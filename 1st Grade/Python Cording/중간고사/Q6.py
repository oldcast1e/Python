#주사위를 꺼냈는데 빨강색이면 종료
#파랑색이면 다시 넣고
#다른 색이면 숫자를 확인해 6이면 꺼내는 횟수를 1 증가

leave = 0 #잔돈
k = 0 #꺼낸 횟수

m = int(input()) #입력한 돈
leave += m

while leave>0:
    
    col = input()
    if ("RED" != col):
        
        num = int(input())
        if ("BLUE"
            == col):
            leave -= 500
            
        elif (num ==6):
           k+=2
                  
        else:
            num = int(input())
            k +=1
            leave -= 500
            
    elif("RED" == col):
        
        break
    
print(k)
