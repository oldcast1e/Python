# "sw"과목 성적은 출석(10%),과제(30%),시험(60%)로 구성
"""한 학기 동안 푸틴이 획득한 출석,과제, 시험 점수를 각각 
100점만점 기준으로 입력받는다. 입력받은 각 항목 점수를 
구성된 비율로 환산하여 총합을 출력한 후,

총합이 60점 이상이면 'pass'를 출력 미만이면 'FAIL'을 출력하라"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

total = 0

total += n1*0.1
total += n2 *0.3
total += n3*0.6

sum  = int(total)
print()
print(sum,'\n')

if total>=60:
    print("PASS")
else:
    print("FAIL")