import math
pi = math.pi
print("원의 둘레와 넓이는 구하는 프로그램")
r = float(input("원의 반지름 입력>> "))

print("반지름이 10인 원 둘레의 길이는 {:.5f}이고 넓이는 {:.4f}입니다."
      .format(2*pi*r , pi*r*r))