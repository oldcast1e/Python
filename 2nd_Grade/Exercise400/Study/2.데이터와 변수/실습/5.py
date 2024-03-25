#이름, 이메일, 전화번호, 주소를 입력 받아서 한 줄에 출력
print("이름, 이메일, 전화번호, 주소를 입력 받는 프로그램")
name = input("이름 입력>> ")
email = input("이메일 입력>> ")
phone = input("전화번호 입력>> ")
addr = input("주소 입력>> ")

print("{:-^30}".format('결과'))
print("%-10s %-20s %-20s %-20s" %("name", "email", "phone", "address"))
print("%-10s %-20s %-20s %-20s" %(name, email, phone, addr))


'''
--------------
'''