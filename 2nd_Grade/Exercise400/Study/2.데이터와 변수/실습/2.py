import math
pi = math.pi
print('원의 둘레와 넓이를 구하는 프로그램')
r = (float)(input('원의 반지름 입력>>'))
# print("반지름이 %d인 원 둘레의 길이는 %f이고 넓이는 %f입니다."%(r,2*pi*r,r*r*pi))
print("반지름이 {}인 원 둘레의 길이는 {}이고 넓이는 {}입니다.".format(round(r),round(2*pi*r,5),round(r*r*pi,4)))