#로또 3/9
import random

ml  =[0]*3
for i in range(3):
    ml[i] = int(input())

lw = random.sample(range(1,10),3)

A = set(ml)
B = set(lw)
n = len(A&B)
if n==0:
    print("꽝!")
else:
    print(4-n,"등 당첨")