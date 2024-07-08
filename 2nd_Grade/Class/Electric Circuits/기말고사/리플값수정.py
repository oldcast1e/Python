from scipy.signal import cheby1

def design_cheby_filter(passband, stopband, target_ripple):
    # 체비셰프 필터 설계 함수
    fs = 1000  # 샘플링 주파수 (Hz)
    order = 2  # 필터 차수
    
    # passband, stopband를 Hz에서 rad/s로 변환
    passband_rad = [freq / (fs / 2) for freq in passband]
    stopband_rad = [freq / (fs / 2) for freq in stopband]
    
    # 주어진 target_ripple 값에 대해 Chebyshev 필터 설계
    b, a = cheby1(order, target_ripple, stopband_rad, btype='bandstop', analog=False)
    
    return b, a

# 예시: passband와 stopband 주파수 설정
passband = [9, 31]  # 로우 패스 필터 통과 대역 (10Hz ~ 30Hz)
stopband = [19, 21]  # 밴드 리젝트 필터 차단 대역 (20Hz 주변)

# 목표 리플 값 설정 (예: 0.5)
target_ripple = 0.5

# Chebyshev 필터 설계 함수 호출
b, a = design_cheby_filter(passband, stopband, target_ripple)

# 결과 출력
print(f'Chebyshev 필터 설계 결과:')
print(f'- Passband: {passband} Hz')
print(f'- Stopband: {stopband} Hz')
print(f'- Target Ripple: {target_ripple}')
print(f'- Filter Coefficients (b): {b}')
print(f'- Filter Coefficients (a): {a}')
