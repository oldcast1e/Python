# 두 수를 입력받고 교환하는 알고리즘_1: 추가 변수 사용

n1 = int(input())
n2 = int(input())

b = n2
n2 = n1
n1 = b
print(n1,n2)
# 두 수를 입력받고 교환하는 알고리즘_2: 튜플 이용

n1 ,n2 = n2, n1
print(n1,n2)

