info = []
dic ={}

schoolyear = [1,2,3,4,5]
while True:
    u = input()
    if u == "i":
        sn = int(input()) #학번
        if len(str(sn)) != 8:
            print("id error")
            continue
        name = input() #이름
        sy = int(input()) #학년
        if sy not in schoolyear:
            print('grade error')
            continue
        msub = input() #전공
        enterschoolyear = str(20)+str(str(sn)[0:2])
        k= (name,enterschoolyear,sy,msub)
        dic[sn] = list(k)
        continue
    elif u == "c":
        sn = int(input())

        if sn not in dic:
            print('no id')
            continue
        else:
            N = int(input()) #1,2,3중 하나 입력
            if N == 1:
                name = input()
                dic[sn][0] = name
            elif N == 2:
                sy2 = int(input())
                if sy2 not in schoolyear:
                    print('grade error')
                    continue
                elif sy2 in schoolyear:
                    dic[sn][2] = sy
            elif N ==3:
                msub = input()
                dic[sn][3] = msub
        continue
    elif u =='p':
        sn = int(input())
        if sn not in dic:
            print('no id')
            continue
        print("id %d name is %s"%(sn,str(dic[sn][0])))
        print("id %d entered the school in %d"%(sn,int(dic[sn][1])))
        print("id %d grade is %d"%(sn,int(dic[sn][2])))
        print("id %d major is %s"%(sn,str(dic[sn][3])))
        continue
    
    elif u == 'q':
        print("end")
        break

    else:
        print("no button")
        continue
