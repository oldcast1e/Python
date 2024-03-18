""" a = (1,2,3,4,5)
n = int(input())
b = a*n
print("b = ",b)
print(b.count(3)) """
#튜플 슬라이스
""" mt = (1,2,3,4,5,6,7,8,9)
n1 = int(input())
n2 = int(input())
print(mt[n1:n2]) """
#튜플 오름차순 정렬
mt = (1,9,7,3,2,4,8,5,6)
ml = list(mt)
ml2 = ml.sort()
mt2 = tuple(ml2)
print(mt2)