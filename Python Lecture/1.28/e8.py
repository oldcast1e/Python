dic = {'salmon roe':1000, 'red sea bream':3000,
        'egg roll':1000,'shrimp':2000,'kimbab':1000,
        'tuna':5000}
total = 0
n = int(input())
for i in range(n):
    u = input()
    if u in dic:
        total += dic[u]
print("Total price =",total)