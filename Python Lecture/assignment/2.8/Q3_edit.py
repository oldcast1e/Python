dic = {}
sy_list= [1,2,3,4,5]

while True:
    u = input() #명령어

    if u == "i":
        sn = int(input()) #학번
        if len(str(sn)) != 8:
            print("id error")
            continue

        name = input() #이름
        sy = int(input()) #학년
        if sy not in sy_list:
            print('grade error')
            continue
        ms = input() #전공

        entered_school = '20'+str(sn)[0:2]#입학년도
        
        info = name,entered_school,sy,ms
        dic[sn] = list(info)
    
    elif u =="c":
        sn = int(input())

        if sn not in dic:
            print("no id")
        else:
            n = int(input()) #수정 

            if n == 1:
                name_edit =input()
                dic[sn][0]= name_edit
            elif n == 2:
                sy_edit = int(input())
                if sy_edit not in sy_list:
                    print('grade error')
                    continue
                """ entered_school_edit = str(20)+str(sy_edit)[0:2]
                dic[sn][1] = entered_school_edit """
                dic[sn][2] = sy_edit
            elif n ==3:
                ms_edit = input()
                dic[sn][3] = ms_edit 
    
    elif u =="p":
        sn = int(input())
        if sn not in dic:
            print("no id")
            continue
        
        print("id %d name is %s"%(sn,str(dic[sn][0])))
        print("id %d entered the school in %d"%(sn,int(dic[sn][1])))
        print("id %d grade is %d"%(sn,int(dic[sn][2])))
        print("id %d major is %s"%(sn,str(dic[sn][3])))
    
    elif u =="q":
        print("end")
        break

    else:
        print("no botton")
        continue
