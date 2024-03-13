""" 자연수 변수 num을 입력 받고 for 문을 이용하여
제곱수 num * num의 값을 구하기 위해 연산자 + 를 이용하여 프로그램을 작성하라.

[입력 예시 1]
6

[출력 예시 1]
Result = 36

[입력 예시 2]
10
10
[출력 예시 2]
Result = 100 """

num = int(input())
total = 0  
for i in range(1,num+1):
    total += num
print("Result = ",total)
