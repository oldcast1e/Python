#상대 평가_1: 함수를 통해 오름차순
sn = 8
score = [0]*sn

for i in range(sn):
    score[i] = int(input('Score %d = '%(i+1)))

for j in range(sn-1):
    for i in range(j+1,sn):
        if score[i]>score[j]:
            k = score[j]
            score[j] = score[i]
            score[i] = k
for i in range(sn):
    print("%3d"%(score[i]))
