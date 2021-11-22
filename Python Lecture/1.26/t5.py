""" p =[]
max = 0
n = int(input())
for i in range(n):
    c1 = int(input())
    if len(p)==3:
        if c1>p[0]:
            p.pop(0)
            p.insert(0,c1)
    else:
        p.append(c1) 

    c2 = int(input())
    if len(p)==3:
        if c2>p[1]:
            p.pop(1)
            p.insert(1,c2)
    else:
        p.append(c2)

    c3 = int(input())
    if len(p)==3:
        if c3>p[2]:
            p.pop(2)
            p.insert(2,c3)
    else:
        p.append(c3)
    
    print(p)
for i in range(1,n+1):
    if p[i-1] > max:
        if p[i-1] == p[i]:
            break
        else:
            max = p[i-1]
print("Person%d Win" %(i))

    



 """

p = [0,0,0]

n = int(input())

for j in range(n):
    for i in range(3):
        card = int(input())
        if p[i] < card:
            p[i] = card
    print(p)

max = 0
idx = 0
for i in range(len(p)):
    if max < p[i]:
        max = p[i]
        idx = i
print("Person%d Win" %(idx+1))