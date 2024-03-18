num = int(input())
result = 0
while num >0:
    result *= 10
    result += int(num%10)
    num = int(num/10)
print("Result = ",result)    
