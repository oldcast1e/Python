n = int(input())


max=[0]*3
name = ['a']*3
a = []
b = [0]*3
for j in range(n):
    na = input()
    total = 0
    for i in range(3):
        s = int(input())
        total += s
        if max[i]<s:
            max[i] = s
            name[i] = na
            b[i] = j
    avg = int(total/3)
    a.append(avg) 

print('Korean high score = %s'%name[0])
print("%s's Avg = %d"%(name[0],a[b[0]]))

print('English high score = %s'%name[1])
print("%s's Avg = %d"%(name[1],a[b[1]]))

print('Math high score = %s'%name[2])
print("%s's Avg = %d"%(name[2],a[b[2]]))