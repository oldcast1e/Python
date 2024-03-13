fish_name = ['selmon roe','red bream', 
            'egg roll','shimp','kimbab', 'tuna']
fish_price = [1000,3000,1000,2000,1000,5000]

price = 0
for i in range(len(fish_name)):
    price += fish_price[i]
print("Total price is",price)

fp = 0
price = 0
for fp in fish_price:
    price += fp
print("Total price is",price)    