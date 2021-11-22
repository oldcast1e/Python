#리스트 정렬

a = [5,4,2,8,7]
print("리스트 값: ",a)
print()

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j] < a[i]:
            b = a[i]
            a[i] = a[j]
            a[j] = b
    print(i,a)
print("정렬된 리스트 값: ",a)