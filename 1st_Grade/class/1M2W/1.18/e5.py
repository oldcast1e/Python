# 리스트 요소의 길이/ 합 구하기
""" a = [2,3,4,1,7]
l = 0
s= 0
print(len(a))
print(sum(a))
print("--------")
for i in a:
    l +=1
for k in range(l):
    s += a[k]
    print(s)
print("리스트의 길이: ",l)    
print("리스트 요소의 합: ",s) """
#리스트의 최대.최소 구하기
print("리스트의 최댓값 구하기_반복문")
a = [99,100,81,73,45,68,89,76,51]
m = a[0]
n = a[0]
for i in range(len(a)):
    if a[i] > m:
        m = a[i]
print (m)
print("리스트의 최솟값 구하기_반복문")
b = [99,100,81,73,45,68,89,76,51]
for k in range(len(a)):
    if a[k] < n:
        n = a[k]
print(n)
print("리스트의 최댓값 구하기_내장함수")
print(max(a))
print("리스트의 최솟값 구하기_내장함수")
print(min(a))
