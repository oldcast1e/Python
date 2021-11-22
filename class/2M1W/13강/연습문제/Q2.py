"""SW성적은 출석10% 과제30% 시험60%비율로 구성.
한 학기동안 학생들이 획득한 출석,과제,시험 점수를 각각 100점 만점 기준으로 입력받아
구성된 비율대로 환산하여 총합을 계산한다.

SW과목을 가르치는 교수님은 SW과목을 수강한 모든 학생들의 번호와 출석,과제,시험 점수를
학생 수 만큼 반복하여 입력받고, 총합 점수를 계산하고 통합 점수를 기준으로 등수에
따라 학점을 주기전에 스택 그래프를 이용하여 성적을 가시화 하려한다.

단, 학생 수 는 18명으로 가정하고 점수 입력 과정은 random 모듈을 이용하라
"""
import random
from matplotlib import pyplot

ns = 18
ide = [0]*ns #

sc_at = [0]*ns
sc_as = [0]*ns
sc_ex = [0]*ns

score = [] #이중 리스트(학번,출석,과제,시험점수,총합)
for i in range(ns):
    score.append([0]*5)

for i in range(ns):
    ide[i] = i+1
    score[i][0] = i+1
    score[i][1] = random.randint(50,100) *0.1
    score[i][2] = random.randint(50,100) *0.3
    score[i][3]= random.randint(50,100) *0.6
    score[i][4]= score[i][1] + score[i][2] +score[i][3]
for i in range(ns):
    print("%3d = %5.2f %5.2f %5.2f = %5.2f"%(score[i][0],score[i][1],score[i][2],
                                                score[i][3],score[i][4]))

for j in range(ns-1):
    for i in range(j+1,ns):
        if score[i][4] < score[j][4]:
                score[j],score[i] = score[i] ,score[j]

for i in range(ns):
    sc_at[i] = score[i][1]
    sc_as[i] = score[i][2]
    sc_ex[i] = score[i][3]


stack = []
for i in range(3):
    stack.append([0]*ns) #가로18줄에 세로3중

for i in range(ns):
    stack[0][i] = 0
    stack[1][i] += stack[0][i] + score[i][3]
    stack[2][i] += stack[1][i] + score[i][2]    

pyplot.bar(ide,sc_ex,width = 0.5,color = 'red',label = 'Exam',bottom=stack[0])
pyplot.bar(ide,sc_as,width = 0.5,color = 'yellow',label = 'Assigment',bottom=stack[1])
pyplot.bar(ide,sc_at,width = 0.5,color = 'orange',label = 'Attitudence',bottom=stack[2])

pyplot.xlabel('Identity')
pyplot.xticks(ide)
pyplot.ylabel('Total Score')

pyplot.legend()
pyplot.show()