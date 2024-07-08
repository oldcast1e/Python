import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, sosfreqz

# Time variable settings
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time for 1 second

# Generate original signal
x_t = np.sin(2 * np.pi * 10 * t) + 2 * np.cos(2 * np.pi * 30 * t)

# Generate noise signals
n1_t = 3 * np.sin(2 * np.pi * 20 * t)
n2_t = np.random.normal(0, 0.01, t.shape)

# Composite signal
y_t = x_t + n1_t + n2_t

# Band reject filter design function
def band_reject_filter(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], btype='bandstop', output='sos')
    return sos

# Filter application and simulation function
def apply_filter(y_t, sos):
    y_filtered = sosfilt(sos, y_t)
    return y_filtered

# Simulation to find optimal component values
def find_optimal_values(y_t, target_freq, bandwidth, fs):
    best_sos = None
    best_rmse = float('inf')
    best_params = (0, 0)  # Initial values
    
    for lowcut in np.arange(target_freq - bandwidth, target_freq - 1, 0.5):
        for highcut in np.arange(target_freq + 1, target_freq + bandwidth, 0.5):
            sos = band_reject_filter(lowcut, highcut, fs)
            y_filtered = apply_filter(y_t, sos)
            rmse = np.sqrt(np.mean((y_filtered - x_t)**2))
            if rmse < best_rmse:
                best_rmse = rmse
                best_sos = sos
                best_params = (lowcut, highcut)
    
    return best_sos, best_rmse, best_params

# Find optimal filter component values
target_freq = 20  # Center frequency to remove
bandwidth = 5  # Bandwidth
best_sos, best_rmse, best_params = find_optimal_values(y_t, target_freq, bandwidth, fs)

# Apply optimal filter
y_opt_filtered = apply_filter(y_t, best_sos)

# Filter frequency response
w, h = sosfreqz(best_sos, worN=2000, fs=fs)

# Calculate optimal component values (adjust based on actual circuit)
lowcut, highcut = best_params
R = 1  # Resistance value (default 1 ohm)
C = 1 / (2 * np.pi * highcut * R)  # Capacitance calculation
L = R / (2 * np.pi * lowcut)  # Inductance calculation

# Visualization of results
plt.figure(figsize=(15, 10))

plt.subplot(4, 1, 1)
plt.plot(t, x_t)
plt.title('Original Signal')

plt.subplot(4, 1, 2)
plt.plot(t, y_t)
plt.title('Signal with Noise')

plt.subplot(4, 1, 3)
plt.plot(t, y_opt_filtered)
plt.title('Filtered Signal')

plt.subplot(4, 1, 4)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()

plt.tight_layout()
plt.show()

# Output optimal RMSE and component values
print(f'Optimal RMSE: {best_rmse}')
print(f'Optimal Component Values: R = {R} Ω, L = {L:.2e} H, C = {C:.2e} F')