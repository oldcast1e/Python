xp2 = int(input())
yp2 = int(input())

xm2 = int(input())
ym2 = int(input())

xr = int(input())
yr = int(input())

gn = int(input())

score = 0
cx = 0
cy = 0

while gn > score:
    u = input()
    
    if u == "UP":
        cy += 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif (cx != xp2 or cy != yp2) or (cx != xm2 or cy != ym2): #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
          
        elif score>=3:
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
    
    elif u == "DOWN":
        cy -= 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif (cx != xp2 or cy != yp2) or (cx != xm2 or cy != ym2): #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
        elif score>=3:
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))

    elif u == "LEFT":
        cx -= 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif (cx != xp2 or cy != yp2) or (cx != xm2 or cy != ym2): #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
            elif score>=3:
                    break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))

    elif u == "RIGHT":
        
        
        if score<3:
            cx += 1
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif (cx != xp2 or cy != yp2) or (cx != xm2 or cy != ym2): #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
        elif score>=3:
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))

    elif u == "LEFTUP":
        cx -=1
        cy += 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif (cx != xp2 or cy != yp2) or (cx != xm2 or cy != ym2): 
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
        elif score>=3:
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))

    elif u == "LEFTDOWN":
        cx -=1
        cy -= 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif not  cx != xp2 or cy != yp2 or cx != xm2 or cy != ym2: #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))

    elif u == "RIGHTUP":
        cx +=1
        cy += 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif not  cx != xp2 or cy != yp2 or cx != xm2 or cy != ym2: #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
        elif score>=3:
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))

    elif u == "RIGHTDOWN":
        cx +=1
        cy -= 1
        
        if score<3:
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            if cx == xp2 and cy == yp2: #1
                score +=2
            elif cx == xm2 and cy == ym2: #2
                score -=2

            elif cx == xr and cy == yr: #3
                cx = 0
                cy = 0

            elif not  cx != xp2 or cy != yp2 or cx != xm2 or cy != ym2: #4
                if cx*cy>0:
                    score +=1
                elif cx*cy<=0:
                    score -=1
                break
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
    
    else:
        continue
