""" 임의의 자연수 n을 입력 받고
n의 각 자리수의 총합을 구하여 반환하는 함수를 작성하고
테스트 프로그램을 작성하라.

# 호출 프로그램 (함수 호출 예시)
n = int(input())
result = sum_digit(n)
print(result)


[입력 예시 1]
123

[출력 예시 1]
6

[입력 예시 2]
4953

[출력 예시 2]
21 """

num = int(input())
result = 0
t =0
def re(n):
    while num>0:
        result *= 10
        result += int(num%10)
        t += result
