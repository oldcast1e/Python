n = int(input()) #양의 정수(입력값)
m = int(input()) #확인값
i = 1
while i <= n:
    cnt = 0
    for j in str(i):
        if j.find(str(m)) != -1:
            cnt += 1
    if cnt == 0:
        print(i)
    else:
        print("clap!" * cnt)
    i += 1