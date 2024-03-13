mn = int(input())

fid = open("list",'w')
print("<메뉴 입력>")
for i in range(mn):   
    mname = input("메뉴이름: ")
    mprice = input("메뉴 가격: ")
    fid.write("%s : %s"%(mname,mprice)+'\n')
fid.close()
fid = open("list",'r')
result = fid.read()
fid.close()
print("<메뉴판>")
print(result)

