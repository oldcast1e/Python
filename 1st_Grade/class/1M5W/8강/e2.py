dic = {'name': '이헌성','age': '20','adress':'수원'}
N = int(input())
for i in range(N):
    u = input("수정을 원한다면 r, 삭제를 원한다면 d, 취소하고 싶으시다면 c를 눌러주세요: ")
    if u == 'r':
        k = input("수정을 원하시는 키를 입력해주세요:")
        value = input("새로운 값을 입력해주세요.")

        dic[k] = value

    elif u == 'd':
        k = input("삭제를 원하시는 키를 입력해주세요:")
        del dic[k]

    elif u == 'c':
        print("취소하겠습니다.")

    else:
        print("키를 확인해주세요.")

key = input("원하는 정보를 입력하세요: ")

if key in dic:
    print(key,':',dic[key])
else:
    print("해당되는 정보가 존재하지 않습니다.")

