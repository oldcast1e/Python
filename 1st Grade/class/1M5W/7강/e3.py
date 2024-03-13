""" n = int(input())

for j in range(n):
    total = 0 
    for i in range(3):
        u = int(input())
        total += u
        result = round(total/3,2)
    print("avg",j+1,"=",result) """

    # 각 학생별 국영수 점수 한번에 입력

score = []
n = int(input("학생의 수: "))

for j in range(n):
    s = input("모든 점수를 입력하세요:").split(" ")
    score.append(s)

for i in range(n):
    total = 0
    for j in range(3):
        total += int(score[i][j])
    avg = round(total/3,2)
    print("Avg = ",avg)

    



