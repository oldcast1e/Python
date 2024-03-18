sm = int(input()) #투입한 돈
pr = int(input()) #물건 값

b = sm - pr #잔돈
k = b
p500 = 0
p50 = 0
p10 = 0

while True:
    if b // 500 >=1:
        p500 +=1
        b -= 500
        continue
    elif b // 50 >=1:
        p50 +=1
        b -= 50
        continue
    elif b//10 >=1:
        p10 +=1
        b -= 10
        continue
    else:
        break
print('balance =',k)    
if p500>0:
    print("500won :",p500)
if p50>0:
    print("50won :",p50)
if p10>0:
    print("10won :",p10)    
