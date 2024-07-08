print("성적 출력 프로그램입니다.")
user = input("성명 입력>>")
score1 = float(input("국어 성적>> "))
score2 = float(input("영어 성적>> "))
score3 = float(input("수학 성적>> "))

sum = score1 + score2 + score3

print("{:-^30}".format("계산결과"))
print("성명 : {}".format(user))

print("국어 : {:.0f}".format(score1))
print("영어 : {:.0f}".format(score3))
print("수학 : {:.0f}".format(score3))
print("총점 : {:.0f}".format(sum))
print("평균 : {:.1f}".format(sum/3))

