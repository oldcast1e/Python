n1 = int(input())
n2 = int(input())

a = []
b = []
for j in range(n1,n2+1):    
    for i in range(1,10):
        a.append("%d * %d = %2d"%(j,i,j*i))
        
for j in range(n2-n1+1):
    b.append(a[j*9:j+9+(j*8)])
print(b)
print()
for j in range(len(b)): #3번 반복
    c = []
    for i in range(10): #10번 반복
        for k in range(len(b)):
            c.append(b[k][i])
        
    
