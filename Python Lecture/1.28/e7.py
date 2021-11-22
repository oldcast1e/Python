sbj = {}
n = int(input())
for i in range(n):
    s = input().split(" ")
    sbj[i] = s

total_SW= 0
total_OS = 0
total_DB = 0

for k in range(3):
    for j in range(n):
        if k == 0:
            total_SW += int(sbj[j][k])
        elif k == 1:
            total_OS += int(sbj[j][k])
        elif k == 2:
            total_DB += int(sbj[j][k])

print("Average(SW) =",total_SW//n)
print("Average(OS) =",total_OS//n)
print("Average(DB) =",total_DB//n)