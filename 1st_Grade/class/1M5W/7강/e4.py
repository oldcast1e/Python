score = []
n = int(input("학생 수를 입력하세요: "))

for i in range(n):
    s = input("모든 점수를 입력하세요: ").split(" ")
    score.append(s)

max = 0
for i in range(n):
    total = 0
    for j in range(3):
        total += int(score[i][j])
        
        if max < total:
            max = total
avg = round(max/3,2)
print("Avg = ",avg)

