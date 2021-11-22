n = int(input())
m = int(input())
k = 1
while n>=k:
    if k == m:
        print('clap!')
    
    if k//10 == m:
        print('clap!')

    else:
        for i in range(1,10):
            if k%(10*i)==m:
                print('clap!')
    k +=1

