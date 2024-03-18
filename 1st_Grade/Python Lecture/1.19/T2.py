num = int(input())

to = 0
te = 0

for i in range(1,num+1):
    if i%2==0:
        te = te +i
    else:
        to = to + i
print("Sum1 = ",to)
print("Sum2 = ",te)