""" a = [[1,2,3],[4,5,6],[7,8,9]]
b = [9,8,7,6,5,4,3,2,1]

print(reversed(b))
k = reversed(b)
print(list(k))
print("확장 슬라이싱")
print(b[::-1]) """

la = ['a','b','c','d']
print("단순 출력")
print(la)
print('변환 출력')
x= enumerate(la)
print(x)
k =list(x)
print(k)
for i,j in enumerate(la):
    print(i,j)