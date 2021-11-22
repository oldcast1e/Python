fish_name = ['selmon roe','red bream', 
            'egg roll','shimp','kimbab', 'tuna']
fish_price = [1000,3000,1000,2000,1000,5000]

n = int(input())
rotate = n//6 #n이 10일때 1
l = n%6 #n이 10일때 4
total = 0 
for i in range(rotate):
    for j in range(6):
        total += fish_price[j]
for j in range(l):
    total += fish_price[j]
print("Total price is",total)