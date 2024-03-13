a = []
m =[]
n1 = int(input("dia = "))
a.append(n1)
m.append(100)

n2 = int(input("ruby = "))
a.append(n2)
m.append(50)

n3 = int(input("sapphire = "))
a.append(n3)
m.append(70)
#345

total = 0
for i in range(len(a)):
    total += a[i]*2*m[i]
print("Total = ",total)





