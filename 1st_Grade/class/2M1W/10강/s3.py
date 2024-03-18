# "sw"과목 성적은 출석(10%),과제(30%),시험(60%)로 구성
"""한 학기 동안 푸틴이 획득한 출석,과제, 시험 점수를 각각 
100점만점 기준으로 입력받는다. 입력받은 각 항목 점수를 
구성된 비율로 환산하여 총합을 출력한 후,

총합이 90이상이면A,80이상이면B,70이상이면C,60이상이면D,아니면 F출력"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

total = 0

total += n1*0.1
total += n2 *0.3
total += n3*0.6

sum  = int(total)
print("sum =",sum,'\n')
if sum >=90:
    print("A")
elif sum>=80:
    print("B")
elif sum>=70:
    print('C')
elif sum>=60:
    print('D')
else:
    print("F")