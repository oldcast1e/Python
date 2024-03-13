#양의 정수입력
#확인값 입력 -->확인값이 들어간 숫자의 경우 박수(각 자리마다)
n = int(input())
m = int(input())

c = 1
while n>=c:
    cnt = 0
    for j in str(c):       
        if j.find(str(m)) != -1:#-1이 아니라는 건 0--> find는 문자의 위치를 찾음 = 0임 = 0의 위치에 있음 = 찾고자 하는 문자 존재
            cnt += 1 #찾은 횟수
        
    if cnt == 0:
        print(c)
    else:
        for i in range(cnt):
            print("Clap!!")
    c+=1
