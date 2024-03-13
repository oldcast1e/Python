user_info = { 'name':'David', 'age':21, 'address':'Gwangjin-gu, Seoul' }
u = input()
if u == 'age':
    print('age :',user_info[u])
elif u== 'name':
    print('name :',user_info[u])
elif u == 'adress':
    print('adress :',user_info[u])
else:
    print("The info does not exist!")