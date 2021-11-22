import math as cal                       #my_calmodule 모듈 재사용 선언
import random                                    #random 모듈 재사용 선언

while True:                                      #무한루프
    print("***사칙연산 퀴즈를 시작합니다.***")   #퀴즈 시작을 알리는 print()
    op = input("어떤 연산을 하고 싶은가요? : ")  #연산자를 입력하고 op에 저장

    if op not in ["+","-","*","/"]:                     #연산자를 잘못 입력했으면
        print("잘못 입력하였습니다.\n다시 입력하세요.") #잘못 입력되었다는 문구 출력
        continue                                        #continue문 실행
    else:                                               #연산자 입력이 올바르게 되었다면

        num1 = random.randint(0,99)                     #0~99 사이의 임의의 수 생성
        num2 = random.randint(0,99)                     #0~99 사이의 임의의 수 생성

        if num2 == 0:                            #num2의 값이 0이면(나눗셈에서 분모는 0이 될 수 없음)
            print("나누는 값이 0이면 안됩니다.\n다시 입력하세요.") #잘못 입력되었다는 문구 출력
            continue
        else:
            #퀴즈의 내용 출력 및 입력값을 int()형변환 후 result에 대입
            result = int(input("%d %s %d 의 결과는 얼마입니까?"%(num1,op,num2)))

        if op == "+":                              #op값이 "+"랑 같으면
            answer = cal.calPlus(num1,num2)        #calplus() 함수 호출
            
        if op == "-":                              #op값이 "-"랑 같으면
            answer = cal.minus(num1,num2)       #calminus() 함수 호출
                       
        if op == "*":                              #op값이 "*"랑 같으면
            answer = cal.calmulti(num1,num2)       #calmulti() 함수 호출
            
        if op == "/":                              #op값이 "/"랑 같으면
            #caldiv() 함수 호출. caldiv()함수는 몫만 계산하는 기능을 함
            answer = cal.caldiv(num1,num2)

        if result == answer:                       #result값과 answer값이 같으면
            print("정답입니다.")                   #정답 처리 출력
        else:                                      #result값과 answer값이 다르면
            print("틀렸습니다.")                   #오답 처리 출력

        select = input("계속 문제를 푸시겠습니까?(Y/N) ")  #퀴즈 지속여부 입력받아 select에 대입

        if select == "Y" or select == 'y':                 #select의 값이 'Y'이거나 'y'이면
            continue                                       #continue문 실행
        else:                                              #select의 값이 'Y', 'y'이 아니면
            print("문제풀기를 종료합니다.")                #문제풀기 종료 문구 출력
            break                                          #break문 실행 무한루프 탈출
                     