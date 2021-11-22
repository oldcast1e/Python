total = 0
total_1 = 0
total_2 = 0
for i in range(2):
    for j in range(3):
        n = int(input())
        if i == 0:
            total_1 += n
        else:
            total_2 +=n

print('Sejong :',total_1)
print('Daeyang  :',total_2)
r1 = total_1%3
r2 = total_2%3
if r1>r2:
    print('Winner : Sejong')
elif r1<r2:
    print('Winner : Daeyang')
else:
    print("Winner : None")