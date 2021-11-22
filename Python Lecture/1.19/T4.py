""" 자연수 n1과 n2를 입력 받고 중첩 for 문을 이용하여
구구단 n1단부터 n2단 까지 출력하는 프로그램을 작성하라.

[입력 예시 1]
5
6

[출력 예시 1]
5 X 1 = 5
5 X 2 = 10
…
…
5 X 9 = 45
6 X 1 = 6
6 X 2 = 12
…
…
6 X 9 = 54 """

n1 = int(input())
n2 = int(input())


for i in range(1,10):
    print(n1,"X",i,"=",n1*i)
for k in range(1,10):
    print(n1,"X",k,"=",n2*k)