""" 자연수 변수 num을 입력 받고 for 문을 이용하여
1 * 2 * 3 * … * num의 값을 구하는 프로그램을 작성하라.

[입력 예시 1]
5

[출력 예시 1]
Result = 120

[입력 예시 2]
7

[출력 예시 2]
Result = 5040
 """
result= 1
num = int(input())
for i in range(1,num+1):
    result *= i  
print("Result = ",result)