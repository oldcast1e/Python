import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X + 2 + 0.1 * np.random.randn(100, 1)

# 데이터를 텐서로 변환
X_tensor = torch.from_numpy(X).float()
y_tensor = torch.from_numpy(y).float()

# 선형 회귀 모델 정의
class LinearRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)
        
    def forward(self, x):
        return self.linear(x)

# 모델 생성
input_size = 1
output_size = 1
model = LinearRegression(input_size, output_size)

# 손실 함수와 최적화 함수 정의
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 모델 학습
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)
    
    # Backward pass 및 최적화
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 학습된 모델을 사용하여 예측
predicted = model(X_tensor).detach().numpy()

# 결과 시각화
plt.scatter(X, y, label='Original data')
plt.plot(X, predicted, 'r-', label='Fitted line')
plt.legend()
plt.show()
