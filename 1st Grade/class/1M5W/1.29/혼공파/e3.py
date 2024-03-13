#피보나치 수열 만들기
n = int(input())
a = []
for i in range(1,n+1):
    if i == 1:
        a.append(1)
    elif i == 2:
        a.append(1)
    else:
        p = int(a[i-2])+int(a[i-3])
        a.append(p)
print("%d번째 피보나치 수열: %d"%(n,p))