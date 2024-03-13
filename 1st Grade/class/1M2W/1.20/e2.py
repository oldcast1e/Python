#딕션너리 추가 및 제거
Dic = {

}
print("딕션너리 추가 전 값: ",Dic)

Dic ["날짜"] = "2021.1.20"
Dic ["요일"] = "화요일"
Dic ["시간"] = "11:22"

print("딕션너리 추가 후 값: ",Dic)
print()
name = input("확인하고자하는 키 이름:")
if name in Dic:
    print("true")
else:
    print("false")
print()
name2 = input("확인하고자하는 키 이름:")
v = Dic.get("%s"%name2)
print(v)