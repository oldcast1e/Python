print("성적 출력 프로그램입니다.")
name = input("성명 입력>>")
s1 = (int)(input("국어 성적>>"))
s2 = (int)(input("영어 성적>>"))
s3 = (int)(input("수학 성적>>"))
print('----------계산 결과----------')
print(name)
print("국어 성적:",s1)
print("영어 성적:",s2)
print("수학 성적:",s3)
print("총점:",(s1+s2+s3))
print('평균:',(float)(s1+s2+s3)/3)
