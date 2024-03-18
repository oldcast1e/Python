"""한 학기가 끝나고 모든 과목의 성적이 A,B,C,D,F로 확정.
한 학기 동안 열시밓 공부한 트롬프의 성적으로 기반으로 평균 학점을 계산하는 프로그램 작성.

단. 트럼프는 SW(3),OD(3),DB(3),MATH(2),HISTORY(1)을 수강"""

sn = 5
grade = ['C','B','A','C','D']
credit = [3,3,3,2,1]

total_c = 0
total_g =0.0
for i in range(sn):
    total_c += credit[i]
    if grade[i] == 'A':
        total_g += credit[i]*4.0
    elif grade[i] == 'B':
        total_g += credit[i]*3.0
    elif grade[i] == 'C':
        total_g += credit[i]*2.0
    elif grade[i] == 'D':
        total_g += credit[i]*1.0
    elif grade[i] == 'F':
        total_g += credit[i]*0.0
Grade = total_g/total_c
print("Trup = %4.2f"%Grade)
    