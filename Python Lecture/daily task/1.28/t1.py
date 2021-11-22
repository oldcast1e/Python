a = []
bmi = []

N = int(input())
for i in range(N):
    dic = {}
    n = input()
    h = int(input())
    w = int(input())
    dic['name'] = n
    dic['high'] = h
    dic['weight'] = w
    a.append(dic)

for j in range(N):
    BMI = int(int(a[j]['weight'])/((int(a[j]['high'])*0.01)**2))
    
    bmi.append(BMI)

k = bmi.index(min(bmi))
print('Min BMI Member :',a[k]['name']+',',int(bmi[k]))