#이름과 점수를 입력
#상위 25%이내 A,상위 50%이내 B,상위 75이내C,기타D
sn = 8
id_n = [1]*sn
score = [0]*sn


for i in range(sn):
    id_n[i] = int(input("Number = "))
    score[i] = int(input("Grade = "))
for j in range(sn-1):
    for i in range(j+1,sn):
        if score[i]>score[j]:
            k = score[j]
            score[j] = score[i]
            score[i] = k

            t = id_n[i]
            id_n[i] = id_n[j]
            id_n[j] = t 

grade = ['A']*sn
for i in range(sn):
    if i+1 <= sn*0.25:
        grade[i] = "A"
    elif i+1 <= sn*0.50:
        grade[i] = "B"
    elif i+1 <= sn*0.75:
        grade[i] = "C"
    else:
        grade[i] = "D"
for k in range(sn):
    print("%d %3d %s"%(id_n[k],score[k],grade[k]))
""" for i in range(sn):
    print("Student%d's Score: %d"%(id_n[i],score[i])) """