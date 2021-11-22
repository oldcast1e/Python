#로또 6/45
# 중복방지
import random

balls = list(range(1,46))

ml  =[0]*6
wl = [0]*6

k = 0
while 6>k:
    n = int(input())
    random.shuffle(balls)
    if n in ml:
        print("중복 불가, 다시 입력하세요")
    else:
        ml[k]= n

        wl[k] = random.choice(balls) 
        balls = set(balls)
        balls.remove(n)
        balls = list(balls)
        k+=1
balls.sort()
wl.sort()
""" print(balls)
print()    """     
print("내가 작성한 로또",ml)
print("추첨 번호",wl)

A = set(ml)
B = set(wl)
scoren = len(A&B)
if scoren<=3:
    print("꽝!")
else:
    print(7-n,"등 당첨")
