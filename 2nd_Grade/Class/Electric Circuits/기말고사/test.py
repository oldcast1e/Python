import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# 샘플링 주파수 및 시간 벡터 설정
fs = 1000  # 샘플링 주파수 (Hz)
t = np.arange(0, 1, 1/fs)  # 시간 벡터 (0초에서 1초까지 1ms 간격)
num_simulations = 100

def generate_signals():
    # 원신호 생성
    x_t = 1 * np.sin(2 * np.pi * 10 * t) + 2 * np.cos(2 * np.pi * 30 * t)

    # 잡음 신호 생성
    n1_t = 3 * np.sin(2 * np.pi * 20 * t)
    n2_t = np.random.normal(0, 0.1, len(t))  # N(0, 0.01)의 표준편차 0.1
    
    # 입력 신호 생성
    y_t = x_t + n1_t + n2_t
    
    return x_t, y_t, n1_t, n2_t

def design_filters():
    # Band Reject 필터 설계 (20Hz 잡음 제거)
    br_order = 2
    br_cutoff = [19, 21]
    b_br, a_br = butter(br_order, [c / (fs / 2) for c in br_cutoff], btype='bandstop')
    
    # Low Pass 필터 설계 (30Hz 이하 신호 통과)
    lp_order = 2
    lp_cutoff = 30
    b_lp, a_lp = butter(lp_order, lp_cutoff / (fs / 2), btype='low')

    return (b_br, a_br), (b_lp, a_lp)

def apply_filters(y_t, br_filter, lp_filter):
    b_br, a_br = br_filter
    b_lp, a_lp = lp_filter

    # 필터 적용 (Band Reject -> Low Pass)
    y_br_filtered = filtfilt(b_br, a_br, y_t)
    y_filtered = filtfilt(b_lp, a_lp, y_br_filtered)
    
    return y_filtered

def calculate_percentage_error(x_t, y_filtered):
    return np.mean(np.abs((x_t - y_filtered) / x_t)) * 100

# 시뮬레이션 수행
errors = []

br_filter, lp_filter = design_filters()

for _ in range(num_simulations):
    x_t, y_t, n1_t, n2_t = generate_signals()
    y_filtered = apply_filters(y_t, br_filter, lp_filter)
    
    error = calculate_percentage_error(x_t, y_filtered)
    
    errors.append(error)

# 평균 오차 및 표준 편차 계산
mean_error = np.mean(errors)
std_error = np.std(errors)

print(f'두 필터를 거친 후의 평균 오차율: {mean_error:.2f}%, 표준 편차: {std_error:.2f}%')

# 원신호와 필터링된 신호 그래프로 비교
plt.figure(figsize=(12, 6))

plt.plot(t, x_t, label='Original Signal')
plt.plot(t, y_filtered, label='Filtered Signal')
plt.title('Original Signal vs Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
