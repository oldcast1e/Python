""" 임의의 자연수 n을 입력 받고
n의 약수의 개수를 구하여 반환하는 함수를 작성하고
테스트 프로그램을 작성하라.

# 호출 프로그램 (함수 호출 예시)
n = int(input())
result = count_factors(n)
print("The number of factors of %d is %d." % (n, result))


[입력 예시 1]
12

[출력 예시 1]
The number of factors of 12 is 6.

[입력 예시 2]
30

[출력 예시 2]
The number of factors of 30 is 8.
 """

n = int(input())
k = 1

def count_factors(n):
    r = 0
    i = n
    while i >=1:
        if n%i == 0:
            r = r + 1
        i = i-1
    return r

result = count_factors(n)
print("The number of factors of %d is %d." % (n, result))
