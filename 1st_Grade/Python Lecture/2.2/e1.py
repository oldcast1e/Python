n = int(input())
a =[0]*n
t =0
for i in range(n):
    m = int(input())
    if m<0:
        m *= -1
    else:    
        t+=m
    a[i] = m
a.sort()    
print(a)
print("Sum =",t)