dic = {}
N = int(input())
for i in range(N):
    n = input()
    s = int(input())
    dic[n] = s
fn = input()
if fn in dic:
    print(fn+"'s score = ",dic[fn])

