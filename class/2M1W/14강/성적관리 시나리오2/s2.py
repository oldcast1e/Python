score = [0]*2
os = [0]*2
for i in range(2):
    total = 0
    s = input().split(" ")
    os[i] =s
for i in range(2):    
    total += int(os[i][1])* 0.1
    total += int(os[i][2])* 0.3
    total += int(os[i][3])* 0.6

    score[i] = (s[0],total)
    
t2 = open('score1.txt','a')
for i in range(2):
    t2.write(str(score[i][0]))
    t2.write(":")
    t2.write(str(score[i][1]))
    t2.write('\n')
t2.close()
