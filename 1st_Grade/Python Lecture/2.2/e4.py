sn = int(input())
a = []
s = []
for j in range(sn):
    total = 0
    for i in range(3):
        score = int(input())
        total += score
    a.append(total)
for i in range(sn):
    avg = int(a[i])/3
    s.append(avg)
max = 0
min = 100    
for i in range(sn):
    if max<s[i]:
        max = s[i]
    if min>s[i]:
        min = s[i]
print('Highest Avg : %d'%max)
print('Lowest Avg : %d'%min)