""" 정수를 전달 받아 양수이면 1만큼 증가시키고,
음수이면 1만큼 감소시켜 반환하는
함수 enlarge(n)를 작성하고 테스트 프로그램을 작성하라.

# 호출 프로그램 (함수 호출 예시)
n = int(input())

print(enlarge(n))


[입력 예시 1]
3

[출력 예시 1]
4

[입력 예시 2]
-7

[출력 예시 2]
-8 """

n= int(input())

def enlarge(n):
    if n>0:
        c = n+1
        return c
    else:
        d = n-1
        return d

print(enlarge(n))