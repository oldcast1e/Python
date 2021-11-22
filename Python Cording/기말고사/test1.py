N = int(input())
total =1
c = N
for j in range(N+1,1,-1):
    
    for i in range(1,N+1):
        if j%i == 0:
            c-=1
print(c)
