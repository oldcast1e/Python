sn = int(input())
score =[]
for j in range(sn):
    s = input().split(" ")
    score.append(s)

for j in range(sn):   
    total = 0
    for i in range(3):
        total += int(score[j][i])

    avg = round(total/3,2)
    print("Student", i+1,"'s Average Score :",avg) 