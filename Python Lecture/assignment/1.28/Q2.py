dic = {'Americano':1500,'Cafelatte':2000,'Cookie':1000}
total = 0
a = 0
ca = 0
co = 0
while True:
    n = int(input())
    if n==1:
        total += int(dic['Americano'])
        a +=1

    elif n==2:
        total += int(dic['Cafelatte'])
        ca +=1

    elif n==3:
        total += int(dic['Cookie'])
        co +=1

    elif n ==4:
        
        print('Current  sum :',total)

    elif n ==5:
        
        print('Ordered menu')
        print('Americano',a)
        print('Cafelatte',ca)
        print('Cookie',co)
        print('Final sum :',total)
        break
        
    else:
        print('Wrong number')