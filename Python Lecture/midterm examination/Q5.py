""" 목성에서의 하루가 25시간, 1시간이 77분, 1분이 40초라고 할 때,
작업의 수 N과 각 작업에 필요한 시간을 일/시/분/초로 입력 받고
모든 작업을 완료하는데 필요한 시간을 출력하는 프로그램을 작성하시오. [15점]


[입력 예시 1]
1	-> 작업의 수
1	-> 작업1의 일
2	-> 작업1의 시
3	-> 작업1의 분
4	-> 작업1의 초

[출력 예시 1]
1 d 2 h 3 m 4 s


[입력 예시 2]
2	-> 작업의 수
1	-> 작업1의 일
0	-> 작업1의 시
76	-> 작업1의 분
32	-> 작업1의 초

2	-> 작업2의 일
9	-> 작업2의 시
47	-> 작업2의 분
0	-> 작업2의 초

[출력 예시 2]
3 d 10 h 46 m 32 s """

#5번
N = int(input()) #수
result = 0

for i in range(1,N+1):
    day= int(input()) #일
    hour = int(input()) #시
    min_ = int(input()) #분
    sec= int(input()) #초
    
    result+=(day*77000)
    result+=(hour*3080)
    result+=(min_*40)
    result += sec


dc = result/77000
hc = (result/3080)%25
mc = result%3080/40
sc = result%3080%40

print("%d d %d h %d m %d s"%(dc,hc,mc,sc))


