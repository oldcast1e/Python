fish_name = ['selmon roe','red bream', 
            'egg roll','shimp','kimbab', 'tuna']
fish_price = [1000,3000,1000,2000,1000,5000]

m = int(input())

idx = -1
c = 0
p = 0
while True:
    idx +=1
    idx %= len(fish_name)
    if p + fish_price[idx]>m:
        break
    p += fish_price[idx]
    c +=1
print("Total dishes = ",c)