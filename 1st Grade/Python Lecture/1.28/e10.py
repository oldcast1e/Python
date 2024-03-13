Grade = [
['C', 'B', 'A', 'C', 'D'],
['F', 'D', 'C', 'D', 'B'],
['A', 'B', 'A', 'B', 'A'],
['A', 'A', 'B', 'C', 'D'],
['B', 'B', 'B', 'B', 'B'],
['B', 'B', 'C', 'D', 'F'],
['C', 'A', 'A', 'A', 'A'],
['D', 'A', 'A', 'C', 'F']
]

totalscore = []

for i in range(8):
    result = 0
    hs = 0
    for j in range(5):
        if Grade[i][j] == 'A': #SW 3학점
            if j == 0:
                result += 4.0*3
                hs +=3
            elif j == 1:
                result += 4.0*3
                hs +=3
            elif j == 2:
                result += 4.0*3
                hs +=3
            elif j == 3:
                result += 4.0*2
                hs +=2
            elif j == 4:
                result += 4.0*1
                hs +=1

        elif Grade[i][j] == 'B': #OS 3학점
            if j == 0:
                result += 3.0*3
                hs +=3
            elif j == 1:
                result += 3.0*3
                hs +=3
            elif j == 2:
                result += 3.0*3
                hs +=3
            elif j == 3:
                result += 3.0*2
                hs +=2
            elif j == 4:
                result += 3.0*1
                hs +=1
        elif Grade[i][j] == 'C': #DB 3학점
            if j == 0:
                result += 2.0*3
                hs +=3
            elif j == 1:
                result += 2.0*3
                hs +=3
            elif j == 2:
                result += 2.0*3
                hs +=3
            elif j == 3:
                result += 2.0*2
                hs +=2
            elif j == 4:
                result += 2.0*1
                hs +=1
        elif Grade[i][j] =='D': #MATH 2학점
            if j == 0:
                result += 1.0*3
                hs +=3
            elif j == 1:
                result += 1.0*3
                hs +=3
            elif j == 2:
                result += 1.0*3
                hs +=3
            elif j == 3:
                result += 1.0*2
                hs +=2
            elif j == 4:
                result += 1.0*1
                hs +=1
        elif Grade[i][j] == 'F': #HISTORY 1학점
            if j == 0:
                result += 0.0*3
                hs +=3
            elif j == 1:
                result += 0.0*3
                hs +=3
            elif j == 2:
                result += 0.0*3
                hs +=3
            elif j == 3:
                result += 0.0*2
                hs +=2
            elif j == 4:
                result += 0.0*1
                hs +=1
        
    totalscore.append(result/hs)

for i in range(8):
    print("%d %.2f"%(i+1,totalscore[i])) 
