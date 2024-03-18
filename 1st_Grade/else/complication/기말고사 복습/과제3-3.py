#n1와n2값을 입력받고 n1~n2의 구구단을 가로로 출력
n1 = int(input())
n2 = int(input())

for j in range(1,10):
    for i in range(n1,n2+1):
        print("%d x %d = %d"%(i,j,i*j),end='\t')