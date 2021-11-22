import turtle                   #turtle 모듈 재사용 선언

def square(length, color):      #square 함수 정의(사각형 그리기 함수)
    turtle.color(color)         #선색 설정
    for i in range(4):          #사각형 그리기 반복문
        turtle.forward(length)
        turtle.right(90)

#draw_where 함수 정의(어디에서 그릴건지 정함)
def draw_where(x,y):
    color = turtle.textinput("선색","무슨 색으로 그릴 것인가요?")
    length = int(turtle.textinput("선길이","사각형의 길이는 얼마나 되나요?"))
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

while True:                      #무한루프
    #사각형 그리기 문구 출력
    turtle.write("원하는 곳에 사각형 그리기를 시작합니다.")
    #x,y 좌표 설정하기
    x = int(turtle.textinput("x좌표","x좌표값은 얼마인가요?"))
    y = int(turtle.textinput("y좌표","y좌표값은 얼마인가요?"))

    draw_where(x,y)              #draw_where()함수 호출
    #더 그리기 여부 설정하기
    flag = turtle.textinput("그리기여부","계속 그릴건가요?(Y/N)")

    if flag in ["Y","y"]:        #더 그리기를 선택하면
        continue                 #continue문 실행하기
    else:                        #더 그리기를 선택하지 않으면
        #사각형 그리기 종료 문구 출력
        turtle.write("사각형 그리기를 종료합니다.")
        break                    #break문 실행하기