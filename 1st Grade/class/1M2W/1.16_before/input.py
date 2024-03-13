#swap

a = int(input("첫 번째 숫자를 입력하세요:"))
b = int(input("두 번째 숫자를 입력하세요:"))
print("before_swap")
print('first number is',a)
print('second number is',b)
print()
c= a
a = b
b = c
print("after_swap")
print('first number is',a)
print('second number is',b)