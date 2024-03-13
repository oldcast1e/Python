# Type or paste your code in this area
n1 = int(input())
n2 = int(input()) 
for b in range(1,10):
    for a in range(n1,n2+1):
        print("%d * %d = %2d"%(a,b,a*b),end ='\t')
        
