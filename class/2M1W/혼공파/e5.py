import random

h = list("성다나솜현수정재기영재동채연지")

with open("rn","w") as t:
    for i in range(1000):
        name = random.choice(h)+random.choice(h)
        weigh = random.randrange(40,100)
        height =  random.randrange(150,190)

        t.write("{}, {}, {}\n".format(name,weigh,height))