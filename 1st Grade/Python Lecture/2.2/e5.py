a = []
student = {'Denis' : 60, 'Amin' : 70}
N = int(input()) #변경 혹은 추가 횟수

total_stn = len(student)

for i in range(N):
    key = input()
           
    value = int(input())
    
    if key not in student:
        total_stn +=1
        a.append(value)
    student[key] = value

    """ while t1 ==1:
        if 'Denis' in student:
            a.append(student['Denis'])
            t1 =0
    while t2 ==1:
        if 'Amin' in student:
            a.append(student['Amin'])
            t2 =0 """
a.append(student['Denis'])
a.append(student['Amin'])


total = 0
for i in a:
    total += i
avg = round(total/total_stn,2)
print('Average : %.2f'%avg)