n = int(input())
a = []
for i in range(n):
    total =0
    for j in range(3):
        s = int(input())
        total += s
    print("Student",i+1,"point = %.2f"%(total/3))
    avg = round(total/3,2)
    a.append(avg)

m = a[0]
k = a.index(max(a))
print("Highest Score Student =",k+1)
