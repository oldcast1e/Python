""" 두 수를 전달 받아 곱한 값을 반환하는 함수 multiply(n1, n2)와
n1을 n2로 나눈 값을 반환하는 함수 divide(n1, n2)를 작성하고
테스트 하는 프로그램을 작성하라.

# 호출 프로그램 (함수 호출 예시)
n1 = int(input())
n2 = int(input())

print(multiply(n1, n2))
print(divide(n1, n2))


[입력 예시 1]
4
2

[출력 예시 1]
8
2.0

[입력 예시 2]
15
5

[출력 예시 2]
75
3.0 """

n1 = int(input())
n2 = int(input())

def multiply(n1, n2):
     c = n1*n2
     return c

def divide(n1, n2):
    c = n1/n2
    return c

print(multiply(n1, n2))
print(divide(n1, n2))