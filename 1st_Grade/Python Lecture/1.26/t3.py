s = []
n = int(input())
total = 0
for i in range(n):
    sc = int(input())
    s.append(sc)
print(s)
for j in range(n):
    total += s[j]
print("Avg = %.2f" %(total/n))