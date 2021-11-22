n = int(input()) #양의 정수(입력값)
m = int(input()) #확인값
k =1
while n >=k:
    if 10 > k: #k가 1의 자리일때
        if k == m:
            print('clap!') #k가 1일때
        else:
            print(k)
    if k>=10: #k가 10이상의 자리(자리수2이상)
        if k%10 == m: #k의 일의 자리가 m일때
            print('clap!')

        if k//10 == m: #k의 십의 자리가 m일때
            print('clap!')

        elif k//10 != m and k%10 != m :
            print(k)
    k +=1