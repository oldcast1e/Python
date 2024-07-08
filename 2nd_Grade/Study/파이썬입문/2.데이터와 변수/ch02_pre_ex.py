print("::: 나는 65세까지 몇년 남았을까? :::")
user = input("성명 입력: ")
age = int(input("나이 입력: "))

futureAge = 65 - age
print("{:-^30}".format("입력 정보 확인"))

print("{}님은 65세까지 {}년 남았습니다.".format(user,futureAge))