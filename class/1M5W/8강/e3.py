#집합 연산
""" SW = ['SE','OS','DB','DS']
CS = ['SE','AI','CG','HCI']
SW = set(SW)
CS = set(CS)

print('OS'in SW)
print('OS' in CS)
print()
print(SW&CS)
print(SW|CS)
print(SW-CS)
print(CS-SW) """

#집합 고유 연산
SW = ['SE','OS','DB','DS']
CS = ['SE','AI','CG','HCI']
SW = set(SW)
CS = set(CS)

SW.add('DS')
print(SW)
CS.remove('AI')
print(CS)
print()
print(SW.intersection(CS))
print(SW.union(CS))
print(SW.difference(CS))


