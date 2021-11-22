#for반복문과 딕셔너리 사용

Dic = {

}
print("딕션너리 추가 전 값: ",Dic)

Dic ["날짜"] = "2021.1.20"
Dic ["요일"] = "화요일"
Dic ["시간"] = "11:22"
print()
print("for반복문과 딕셔너리 사용")
print()
for i in Dic:
    print(i,":",Dic[i])
    print()