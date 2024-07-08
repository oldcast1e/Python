import numpy as np
from scipy.signal import filtfilt
import matplotlib.pyplot as plt

# 샘플링 주파수 및 시간 벡터 설정
fs = 1000  # 샘플링 주파수 (Hz)
t = np.linspace(0, 1, 1 * fs)  # 시간 벡터 (0초에서 10초까지)

# 원신호 및 필터 계수
x_t = 1 * np.sin(2 * np.pi * 10 * t) + 2 * np.cos(2 * np.pi * 30 * t)
b = [ 0.93849192, -3.72444003,  5.57212849, -3.72444003,  0.93849192]
a = [ 1.        , -3.9567807 ,  5.90224609, -3.93347326,  0.98825389]

# 입력 신호 생성 (원신호 + 잡음)
n1_t = 3 * np.sin(2 * np.pi * 20 * t)
n2_t = np.random.normal(0, 0.1, len(t))  # N(0, 0.01)의 표준편차 0.1
y_t = x_t + n1_t + n2_t

# Chebyshev 필터링 적용
y_filtered = filtfilt(b, a, y_t)

# 평균 절대 백분율 오차(MAPE) 계산
mape = np.mean(np.abs((x_t - y_filtered) / x_t)) * 100

print(f'평균 절대 백분율 오차 (MAPE): {mape:.2f}%')

# 그래프로 시각화
plt.figure(figsize=(10, 6))

# 원신호 및 필터링된 신호 그래프
plt.plot(t, x_t, label='Original Signal')
plt.plot(t, y_filtered, label='Filtered Signal')
plt.title('Original Signal vs Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
