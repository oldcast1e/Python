dic = {}
while True:
    n = int(input())
    if n ==1:
        name = input()
        if name in dic:            
           score = int(input())
           dic[name]=score
        else:
            score = int(input())
            dic[name]=score

    elif n == 2:
        name = input()
        if name not in dic:
            print("No student")
        else:
            print("Name =",name +",","Score =",dic[name])

    elif n == 0:
        break
