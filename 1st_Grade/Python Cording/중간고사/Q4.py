#4번

N = int(input())
A = int(input())
B = int(input())

if(A>B):
    b = B
    B = A
    A = b
    for i in range(A,B+1):
        print("%d X %d = %d" %(N,i,N*i))
elif(A<=B):
    for i in range(A,B+1):
        print("%d X %d = %d" %(N,i,N*i))
    
        
    
