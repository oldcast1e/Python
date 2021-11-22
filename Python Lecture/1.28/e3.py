user_info = { 'name':'David', 'age':21, 'address':'Gwangjin-gu, Seoul' }
n = int(input())
for i in range(n):
    print("Edit #%d"%int(i+1))
    key = input()
    value = input()
    user_info[key] = value
print("USER INFO")
for j in user_info:
    print(j,":",user_info[j])

