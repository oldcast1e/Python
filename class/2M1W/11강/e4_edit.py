#로또 6/45
# 중복방지
#직장인 트럼프가 로또 3등을 이내에 당첨되면 중단, 그 과정까지 의 투자금 확인 코드

import random

win = int(input("당첨 등수(1-5) :"))
count = 0 
while True:
    count +=1
    num = 0
    lotto = random.sample(range(1,46),6)
    lotto.sort()

    ml = random.sample(range(1,46),6)
    ml.sort()
    for i in range(6):  
        if lotto[i] == ml[i]:
            num +=1
    if num == 7-win:
        break
print("시도한 횟수 :",count)
print("투자금 :",(count*0.5),'만원')