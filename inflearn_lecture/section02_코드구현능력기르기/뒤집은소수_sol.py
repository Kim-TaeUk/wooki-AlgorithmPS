x = int(input())
list = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    # for - else 사용
    for i in range(2, x // 2 + 1):  # 중간까지만 돌면 확인 가능
        if x % i == 0:
            return False
    else:
        return True


for x in list:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

# 소수 구하기 -> 1은 소수가 아님! 중간까지만 돌자!
# 숫자 뒤집기 -> 쉬운 방법으로 하자(해설처럼)
