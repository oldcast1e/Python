#5번
N = int(input())
day= int(input())
hour = int(input())
min_ = int(input())
sec= int(input())

result = 0

result+=(day*77000)
result+=(hour*3080)
result+=(min_*40)
result += sec

result *= N

dc = result/77000
hc = (result/77000)%25 +1
mc = result%3080/40
sc = result%3080%40

print("%d d %d h %d m %d s"%(dc,hc,mc,sc))


