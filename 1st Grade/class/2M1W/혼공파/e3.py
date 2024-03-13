#앉힐 수 있는 사람의 최소:2
#않힐 수 있는 사람의 최대:10

#모든 사람의 수:100
n = int(input()) #전체 사람의 수
m = int(input()) #앉을 수 있는 사람의 최솟값
memo = {}
def cf(n,m):
    if n%m != 0:
        k = n/m 
        if 2<=k<=10:
            memo[m] = k  
    else:
        if 2<=n%m <=10:
            k1 = n/m
            k2 = n%m
            

