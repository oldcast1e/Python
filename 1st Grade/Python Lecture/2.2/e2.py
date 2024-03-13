tn = int(input()) #손님의 총인원

for i in range(tn):
    total = 0
    dn = int(input()) #각 손님이 먹은 접시 개수
    for j in range(dn):
        dc = input()
        if dc == 'white':
            total += 1000
        elif dc == 'yellow':
            total += 2000
        elif dc == 'blue':
            total += 3000
        elif dc == 'red':
            total += 5000
    print('Total price =',total)