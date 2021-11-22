a = [0]*3
N = int(input())
for i in range(N):
    for j in range(3):
        n = int(input())
        
        if n > a[j]:
            a[j] = n
    print(a)
k = a.index(max(a))+1
print('Person%d Win'%k)