n = int(input())
k =1
r =1
for j in range(1,n+1): #세로
    for i in range(k): #가로1,2,3,4....(줄)
        print(r,end='')
        r +=1
    print('')
    k+=1