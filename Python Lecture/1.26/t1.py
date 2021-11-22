""" 리스트 a = [2, 3, 1, 4]의 최댓값을 구하는 프로그램을 작성하라.
(단, 내장 함수는 사용하지 않는다.)

[출력 예시]
a = [2, 3, 1, 4]
0 2
1 3
2 3
3 4
Max = 4 """

a = [2,3,1,4]
print("a = ",a)
max =0
for i in range(4):
    if a[i] > max:
        max = a[i]
    print(i,max)
print("Max = ",max)
