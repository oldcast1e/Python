n = int(input())
dic ={}
lt = []#차량이 주차한 시간 리스트

for j in range(n):
    cn = int(input()) #차량 번호
    lt1 = 0
    lt2 = 0
    it = input().split(":") #차량이 들어온 시간
    ot = input().split(":") #차량이 나간 시간

    
    if it[1] > ot[1]: #들어온 시간의 분이 나간 시간의 분보다 클 경우
        lt1 = int(ot[0]) - int(it[0]) -1 #시간
        it[1] = 60 - int(it[1]) #분 계산

        lt2 = int(it[1]) + int(ot[1]) #분
    
    else:
        lt1 = int(ot[0]) - int(it[0]) #시간
        lt2 = int(ot[1]) - int(it[1]) #분
    
    Time = str(lt1)+"h"+" "+str(lt2)+"m"
    dic[cn] = Time

N = int(input())
if N in dic:
    print(dic[N])
else:
    print("None")

