""" 임의의 자연수 n1과 n2를 입력 받고,
두 자연수를 전달 받아 두 자연수의 최대 공약수를 구하여 반환하는 함수를 작성하라.

# 호출 프로그램 (함수 호출 예시)
n1 = int(input())
n2 = int(input())
print(get_gcd(n1, n2))


[입력 예시 1]
4
6

[출력 예시 1]
2

[입력 예시 2]
15
27

[출력 예시 2]
3 """
#dsdssdsddsdsdsdsds
""" # Type or paste your code in this area
def get_gcd(n1,n2):
   i = min(n1,n2)
   while i>1:
       if n1 %i == 0 and n2% i == 0:
            break
        i = i-1
    return i

n1 = int(input())
n2 = int(input())
print(get_gcd(n1,n2)) """

n1 = int(input())
n2 = int(input())

def get_gcd(n1, n2):
    k = min(n1,n2)
    while n1%k != 0 or n2%k !=0:
        k -=1
        if n1%k==0 and n2%k ==0:
            break
    return k

print(get_gcd(n1, n2))
