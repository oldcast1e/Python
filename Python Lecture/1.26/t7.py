n = int(input())
score = []
for i in range(n):
    s = input().split(" ")
    score.append(s)

for i in range(n):
    total = 0
    for j in range(3):
        total += int(score[i][j])

    avg  = round(total/3,2)
    print("Student ",i+1,"s Average Score : ",avg)