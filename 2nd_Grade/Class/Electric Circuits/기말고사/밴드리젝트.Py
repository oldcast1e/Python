import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Updated component values for 20Hz rejection
R = 1e3  # 1 kΩ
L = 1  # 1 H
C = 63.3e-6  # 63.3 µF

# Calculate resonant frequency
f0 = 1 / (2 * np.pi * np.sqrt(L * C))
print(f'Calculated Resonant Frequency: {f0:.2f} Hz')

# Function to calculate frequency response
def calculate_frequency_response(L, C, R=0, fs=1000):
    w0 = 1 / np.sqrt(L * C)
    if R == 0:
        # LC filter
        num = [w0**2]
        den = [1, 0, w0**2]
    else:
        # RLC filter
        num = [w0**2]
        den = [1, R / (L * w0), w0**2]
    
    w, h = freqz(num, den, worN=8000, fs=fs)
    return w, h

# Calculate frequency response for the updated RLC filter
w_rlc, h_rlc = calculate_frequency_response(L, C, R=R)

# Plot frequency response
plt.figure(figsize=(12, 6))

plt.plot(w_rlc, 20 * np.log10(abs(h_rlc)), label='RLC Filter (20Hz Rejection)')
plt.title('RLC Filter Frequency Response (20Hz Rejection)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()