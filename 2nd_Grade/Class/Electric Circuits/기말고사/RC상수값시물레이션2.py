import numpy as np
import matplotlib.pyplot as plt

# 입력 신호 정의
def input_signal(t):
    return 1*np.sin(2*np.pi*10*t) + 2*np.cos(2*np.pi*30*t)

# RC 필터 함수 정의
def rc_filter(t, input_signal, R, C):
    filtered_signal = np.zeros_like(t)
    dt = t[1] - t[0]
    alpha = dt / (R * C)
    for i in range(1, len(t)):
        filtered_signal[i] = (1 - alpha) * filtered_signal[i-1] + alpha * input_signal[i]
    return filtered_signal

# 시뮬레이션 설정
t = np.linspace(0, 1, 1000)  # 1초 동안 1000개의 시간 단계
input_sig = input_signal(t)

# 다양한 RC 상수에 대한 필터링 시뮬레이션 및 결과 저장
R_values = [1000, 5000, 10000]  # 다양한 R 값
C_values = [1e-6, 5e-6, 10e-6]  # 다양한 C 값
filtered_signals = np.zeros((len(R_values), len(C_values), len(t)))
for i, R in enumerate(R_values):
    for j, C in enumerate(C_values):
        filtered_signals[i, j] = rc_filter(t, input_sig, R, C)

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.plot(t, input_sig, 'r-', label='원본 신호')
for i, R in enumerate(R_values):
    for j, C in enumerate(C_values):
        plt.plot(t, filtered_signals[i, j], label=f'RC={R} ohms, {C} F')
plt.title('다양한 RC 상수에 대한 필터링 결과')
plt.xlabel('시간')
plt.ylabel('신호')
plt.legend()
plt.grid(True)
plt.show() 


