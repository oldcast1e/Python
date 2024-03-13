# "sw"과목 성적은 출석(10%),과제(30%),시험(60%)로 구성
"""한 학기 동안 푸틴이 획득한 출석,과제, 시험 점수를 각각 
100점만점 기준으로 입력받는다. 입력받은 각 항목 점수를 
구성된 비율로 환산하여 총합을 출력한 후,

절대평가 방식으로 총합이 90이상이면A,80이상이면B,70이상이면C,60이상이면D,아니면 F출력

"sw"과목으로 가르치시는 교수님은 학생들이 성적을 매기기전에 총합의 평균 점수, 
최고점 및 최하점을 알아버려고한다."""

num_st = 8

At = [90,80,100,70,80,90,100,90]
As = [60,30,90,90,85,80,75,70]
Ex = [85,60,99,100,90,80,70,60]

sum = 0
maximum = 0
minimum = 100

for i in range(num_st):
    at = At[i]
    ass = As[i]
    ex = Ex[i]

    s = int(at*0.1 +ass*0.3 + ex*0.6)
    sum += s
    if s>maximum:
        maximum = s
    if s<minimum:
        minimum = s
avg = int(sum/num_st)
print("Sum =",sum)
print("Avg =",avg)
print("Max =",maximum)
print("Min =",minimum)