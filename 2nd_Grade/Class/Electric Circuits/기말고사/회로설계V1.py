import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# 입력 신호 생성
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 10 * t) + 2 * np.cos(2 * np.pi * 30 * t)
n1 = 3 * np.sin(2 * np.pi * 20 * t)
n2 = np.random.normal(0, 0.1, t.shape)
y = x + n1 + n2

# 저역 통과 필터 설계
def lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y

# 필터 적용
fs = 1000  # 샘플링 주파수
cutoff = 15  # 코너 주파수
filtered_signal = lowpass_filter(y, cutoff, fs)

# 시각화
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, y)
plt.title('Original Signal with Noise')
plt.subplot(3, 1, 2)
plt.plot(t, filtered_signal)
plt.title('Filtered Signal')
plt.subplot(3, 1, 3)
plt.magnitude_spectrum(y, Fs=fs, scale='dB', color='C1')
plt.magnitude_spectrum(filtered_signal, Fs=fs, scale='dB', color='C2')
plt.title('Frequency Spectrum')
plt.tight_layout()
plt.show()