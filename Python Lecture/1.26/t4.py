s = []
total = 0
while True:
    sc = int(input())
    if sc != 0:
        s.append(sc)
        total += sc
    elif sc == 0:
        break
print(s)
print("Avg = %.2f"%(total/len(s)))

