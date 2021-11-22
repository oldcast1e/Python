col = {'white':1000,'yellow':2000,'blue':3000,'red':5000}
total = 0
while True:
    u = input()
    if u in col:
        total += col[u]
    else:
        break
print("Total price = %d"%total)
    
