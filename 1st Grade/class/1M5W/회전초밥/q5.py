fish_name = ['selmon roe','red bream', 
            'egg roll','shimp','kimbab', 'tuna']
fish_price = [1000,3000,1000,2000,1000,5000]

tn = int(input("회전 수를 입력하세요: "))

price = 0
for h in range(tn):
    for i in range(len(fish_name)):
        if fish_name[i] != 'shimp' and fish_price[i] != 1000:
             price += fish_price[i]
print("Total price is",price)
