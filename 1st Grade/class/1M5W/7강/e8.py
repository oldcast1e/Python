#rate를 2,3,4순으로 증가 시킴
# 루프는 3번 반복
nj = 3
jewel = ["diamond","ruby","sapphire"]
cost = [100,50,70]
rate = [2,3,4]
a = [0]*nj


total = 0
for i in range(nj):
    a[i] = int(input())
    total += a[i]*cost[i]*rate[i]
total -= (850+1500)
print("Total = ",total)
