dic = {'ID': 'kylhs0207', 'PW': '26656082'}
id = input("아이디를 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")

if id == dic['ID'] and pw == dic['PW']:
    print("Success!")
else:
    print("Fail. Please Check your Scret Code")