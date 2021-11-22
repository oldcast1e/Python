#리스트 정렬____failure

a = [5,4,2,8,7]
print("리스트 값: ",a)
print()

n = 0
i = 1
while(n<=4):
    for k in range(1,len(a)): #i에 0,1,2,3/ 1,2,3,4
        if a[i] < a[n]:
            b = a[n]
            a[n] = a[i]
            a[i] = b
            if(i<n+1):
                i +=1
            print(a)
            
    n +=1
    i +=1
    
print(a)
