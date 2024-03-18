a = []
for i in range(8):
    n = int(input())
    a.append(n)
    
a.sort(reverse = True)
for j in range(len(a)):
    print(a[j])