fa = open("list",'a')
print("<메뉴 추가>")
for i in range(2):
    mname = input("메뉴이름: ")
    mprice = input("메뉴 가격: ")
    fa.write("%s : %s"%(mname,mprice)+'\n')
fa.close()
fid = open("list",'r')
result = fid.read()
fid.close()
print("<메뉴판>")
print(result)

