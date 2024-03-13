import random

balls = list(range(1,46))

random.shuffle(balls)
# print(balls)

""" c = random.choice(balls)
print(c,'\n') """
s = random.sample(balls,6)
print(s)