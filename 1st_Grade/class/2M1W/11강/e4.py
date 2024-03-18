#로또 6/45
# 중복방지
#직장인 트럼프가 로또 3등을 이내에 당첨되면 중단, 그 과정까지 의 투자금 확인 코드

import random

lotto1 = list(range(1,46))
lotto2 = list(range(1,46))

ml = [0]*6
wl = [0]*6



total = 0
num =0
while num<3:

    for k in range(6):
        ml[k] = 0
        wl[k] = 0
    for i in range(6):
        random.shuffle(lotto1)
        n = random.choice(lotto1) #내가 뽑은 로또
        
        ml[i] = n
        lotto1 = set(lotto1)
        lotto1.remove(n)
        lotto1 = list(lotto1)
    for j in range(6):
        random.shuffle(lotto2)
        m = random.choice(lotto2) #당첨 로또
        
        wl[j] = m
        lotto2 = set(lotto2)
        lotto2.remove(m)
        lotto2 = list(lotto2)

    A = set(ml)
    B = set(wl)
    num = len(A&B)
    total +=5000

print("예상 투자 자본:",total*0.0001)