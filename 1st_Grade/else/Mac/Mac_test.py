for i in range(1,101,1):
    if(i%3==0):
        continue
    else:
        if((i//10)==3 or i%10==3):
            continue
        
    
    print(i,end=',')

