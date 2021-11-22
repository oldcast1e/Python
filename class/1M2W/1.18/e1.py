# 사칙연산 코드 작성
A = int(input("첫번째 숫자를 입력하세요: "))
O = input("연산자를 입력하세요: ")
B = int(input("두번째 숫자를 입력하세요: "))

def cul(a,op,b):
    if op == "+":
        c = a+b
        result =  c
    elif op == "-":
        c = a -b
        result =  c
    elif op == "*":
        c = a *b
        result =  c
    else:
        c == a /b
        result =  c
    return result

k = cul(A,O,B)

print("연산 결과: ",k)