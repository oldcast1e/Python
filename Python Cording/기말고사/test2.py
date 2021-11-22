dic = {}
cnt =0
a = [0]*2
while True:
    
    if cnt == 0:
        for i in range(7):
            u = input()              
            dic[u] = i
        
        cnt =1
        
    if cnt ==1:
        for i in range(2):
            r = input()
            ar = [0]*2
            ar[i] = r
            
                    
            a[i] = dic[r]
        if ar[i] == 'end':
                break
        print(str(a[1])*int(a[0]))
