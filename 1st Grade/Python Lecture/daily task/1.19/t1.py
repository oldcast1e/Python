""" 사용자의 이름, 키(cm), 체중(kg)을 입력받고, 비만지수를 측정해주는 프로그램을 작성하라. 
(단, 소수점 두 번째 자리까지만 출력) 
(BMI 구하는 방법 : 체중 / 키(단위: m)^2)

[입력 예시]
Hong Gill Dong
180
68

[출력 예시]
Hong Gill Dong's BMI is 20.99 """

name = input()
high = float(input())
weight = float(input())

r = weight/(high/100)**2

print("%s's BMI is %.02f"%(name,r))

