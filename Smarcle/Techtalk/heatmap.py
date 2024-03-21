import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 임의의 데이터프레임 생성
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6],
    'D': [6, 5, 4, 3, 2]
}
df = pd.DataFrame(data)

# 히트맵 그리기
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Heatmap using Pandas and Seaborn')
plt.xlabel('Columns')
plt.ylabel('Index')
plt.show()
