# 주머니 속의 주사위를 한번 꺼내는 데 필요한 비용 = 500원
# 돈을 입력받고 돈에 맞추어 주사위를 꺼냄

#주사위를 꺼냈는데 빨강색인 경우 -> 종료
#주사위를 꺼냈는데 파란색인 경우 -> 다시 넣음
#주사위를 꺼냈는데 다른 색인 경우 -> 주사위 숫자 확인 -> 6이면 꺼내는 횟수를 1 증가

#확인 숫자들의 평균을 구하라(단, 소수점아래는 내림하여 정수 부분만 출력한다)

money = int(input())
rate = money//500
result = 0
totalrate = +rate

while rate > 0:
    col = input()
    if col == "RED":
        if totalrate==1:
            break
        
        elif totalrate > 1:
            totalrate -= 1
            break

    elif col == "BLUE":
        rate -= 1
        totalrate -= 1
        
    else:
        num = int(input())
        result += num
        rate -= 1
        if (num == 6):
            rate += 1
            totalrate +=1

if totalrate !=0:
    print(result//totalrate)
elif totalrate == 0 or result == 0:
    print(0)
