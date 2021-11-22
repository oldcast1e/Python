n = int(input())
dic = {}
max = 0
max_city = "a"
for i in range(n):
    N = input() #도시
    pn = int(input()) #인구 수(명)
    mn = int(input()) #면적(만)
       
    x = pn/mn
    if  max<x:
        max = x
        max_city = N

    dic[N] =x
print('Highest Population Density = %s, %.2f'%(max_city,max))


