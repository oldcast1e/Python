fish_name = ['selmon roe','red bream', 
            'egg roll','shimp','kimbab', 'tuna']
fish_price = [1000,3000,1000,2000,1000,5000]

m = int(input())

r = m//13000
ln = m%13000
td = 0
for i in range(r):
    for j in range(6):
        td += 1
while True:
    if ln>=1000:
        ln -= 1000
        td +=1
        if ln<3000:
            break

    elif ln>=3000:
        ln -= 3000
        td +=1
        if ln<1000:
            break

    elif ln>=1000:
        ln -= 1000
        td +=1
        if ln<2000:
            break
    elif ln>=2000:
        ln -= 2000
        td +=1
        if ln<1000:
            break

    elif ln>=1000:
        ln -= 1000
        td +=1

    else:
        break
print("Total dishes = ",td)
    