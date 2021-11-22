sn = int(input())
a = [] #각 과목별 점수
avg_score = [] #모든 학생의 평균 점수
for j in range(sn):
    total = 0
    for i in range(3):
        s = int(input())
        a.append(s)
        total += s
    
    avg_score.append(total/3)

for i in range(sn):
    print('Student'+str(i+1),'point = %.2f'%float(avg_score[i]))
print('Highest Score Student = %d'%(avg_score.index(max(avg_score))+1))
print('Lowest Score Student = %d'%(avg_score.index(min(avg_score))+1))
