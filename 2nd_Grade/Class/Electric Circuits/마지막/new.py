import numpy as np
from scipy.signal import TransferFunction

# Low Pass Filter 소자 값 계산
R_lp = 1  # 저항 (옴)
fc_lp = 35  # 차단 주파수 (Hz)
omega_c_lp = 2 * np.pi * fc_lp

L_lp = R_lp / omega_c_lp
C_lp = 1 / (omega_c_lp**2 * L_lp)

print(f'Low Pass 필터의 소자 값: R = {R_lp} Ω, L = {L_lp:.6f} H, C = {C_lp:.6f} F')

# Low Pass 필터의 차단 주파수 확인
num_lp = [1]
den_lp = [L_lp * C_lp, R_lp * C_lp, 1]
H_lp = TransferFunction(num_lp, den_lp)
w, mag, phase = H_lp.bode()
cutoff_lp = w[np.where(mag <= -3)[0][0]]  # -3dB 지점에서 차단 주파수 선택
cutoff_lp_hz = cutoff_lp / (2 * np.pi)
print(f'Low Pass 필터의 차단 주파수: {cutoff_lp_hz:.2f} Hz')

# Band Reject Filter 소자 값 계산
R_br = 1  # 저항 (옴)
f0_br = 20  # 중심 주파수 (Hz)
BW_br = 5  # 대역폭 (Hz)
omega_0_br = 2 * np.pi * f0_br
BW_rad_br = 2 * np.pi * BW_br

L_br = R_br / BW_rad_br
C_br = 1 / (omega_0_br**2 * L_br)

print(f'Band Reject 필터의 소자 값: R = {R_br} Ω, L = {L_br:.6f} H, C = {C_br:.6f} F')

# Band Reject 필터의 차단 주파수 확인
num_br = [L_br * C_br, 0, 1]
den_br = [L_br * C_br, R_br * C_br, 1]
H_br = TransferFunction(num_br, den_br)
w, mag, phase = H_br.bode()
stopband_start = w[np.where(mag <= -3)[0][0]]  # -3dB 지점에서 차단 대역 시작 주파수
stopband_end = w[np.where(mag <= -3)[0][-1]]   # -3dB 지점에서 차단 대역 끝 주파수
stopband_start_hz = stopband_start / (2 * np.pi)
stopband_end_hz = stopband_end / (2 * np.pi)
print(f'Band Reject 필터의 차단 대역 주파수: {stopband_start_hz:.2f} Hz - {stopband_end_hz:.2f} Hz')