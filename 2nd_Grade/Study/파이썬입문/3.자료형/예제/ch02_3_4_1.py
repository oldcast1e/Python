text = "Hello, World!"

# 특정 문자의 인덱스 찾기
index1 = text.index('H')
index2 = text.index('o')
index3 = text.index('l')

# 결과 출력
print("Index of 'H':", index1)  # 0
print("Index of first 'o':", index2)  # 4
print("Index of 'l':", index3)  # 7

# 찾고자 하는 문자가 문자열에 없는 경우
try:
    index4 = text.index('x')
except ValueError as e:
    print("ValueError:", e)