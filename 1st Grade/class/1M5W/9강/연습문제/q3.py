u = input("문자열을 입력하세요.")


fid = open("python.txt",'w')
fid.write(u)
fid.close()

n = int(input("N입력: "))
m = int(input("M입력: "))
fid = open("python.txt",'r')
fid.seek(n)
print("시작 위치로부터 ",n,"바이트 떨어진 위치에서",m,"바이트만큼 읽은 값:",fid.read(m))
print("파일의 혀재 위치:",fid.tell())
fid.close()