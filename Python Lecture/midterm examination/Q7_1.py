cx = 0
cy = 0

px = int(input())
py = int(input())

mx = int(input())
my = int(input())

rx = int(input())
ry = int(input())

gn = int(input())

score = 0

while gn > score:
    u = input()
    if u == "UP":
        cy+=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue


    elif u == "DOWN":
        cy -=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue
    elif u == "RIGHT":
        cx+=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue
    elif u == "LEFT":
        cx -=1
        
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

    elif u == "RIGHTUP":
        cx +=1
        cy+=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue
    elif u == "RIGHTDOWN":
        cx +=1
        cy-=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

    elif u == "LEFTUP":
        cx -=1
        cy +=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue
    elif u == "LEFTDOWN":
        cx -=1
        cy-=1
        print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
        if cx == px and cy == py:
            if cx != 0 or cy != 0:
                score += 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == mx and cy == my:
            if cx != 0 or cy != 0:
                score -= 2
                print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
                continue
            elif cx == 0 or cy == 0:
                continue
        elif cx == rx and cy == ry:
            cx=0
            cy=0
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue

        else:
            if cx*cy>0:
                score +=1
            elif cx*cy<=0:
                if cx != 0 or cy != 0:
                    score -=1 
                elif cx == 0 or cy == 0:
                    continue
            print("X = %d Y = %d SCORE = %d" %(cx,cy,score))
            continue
            
    else:
        continue

    