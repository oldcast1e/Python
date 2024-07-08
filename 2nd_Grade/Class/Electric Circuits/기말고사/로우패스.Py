from scipy.optimize import minimize

# 목표 차단 주파수
target_fc = 35  # Hz

# 목표 차단 주파수에 맞는 소자 값 계산 함수
def objective(params):
    L, C = params
    calculated_fc = 1 / (2 * np.pi * np.sqrt(L * C))
    return (calculated_fc - target_fc)**2

# 초기 추정값 (기존 소자값을 기반으로)
initial_guess = [10e-6, 20.7e-6]

# 제약조건: L과 C는 양수이어야 함
constraints = [{'type': 'ineq', 'fun': lambda x: x[0] - 1e-9},  # L > 1nH
               {'type': 'ineq', 'fun': lambda x: x[1] - 1e-12}]  # C > 1pF

# 최적화 수행
result = minimize(objective, initial_guess, constraints=constraints, method='SLSQP')

# 최적의 L과 C 값
optimal_L, optimal_C = result.x
optimal_fc = 1 / (2 * np.pi * np.sqrt(optimal_L * optimal_C))

(optimal_L, optimal_C, optimal_fc)