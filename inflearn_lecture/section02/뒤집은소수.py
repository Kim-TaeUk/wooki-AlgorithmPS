x = int(input())
list = list(map(int, input().split()))


def reverse(x):
    # 자릿수 분리하여 list에 저장 : 1234 -> [4, 3, 2, 1] 이렇게 저장됨
    list = []
    while x > 0:
        list.append(x % 10)
        x = x // 10

    # 분리된 자릿수에 10의 len(list)-i-1 제곱하여 res 만들어줌 -> [4, 3, 2, 1]을 4321처럼
    res = 0
    for i in range(0, len(list)):
        res += list[i] * 10 ** (len(list) - i - 1)
    return res


def isPrime(k):
    flag = 0  # flag 도입
    for i in range(2, k):
        if k % i == 0:  # 나누어 떨어지는게 있으면 flag 1로
            flag = 1
            break  # 그리고 바로 반복문 탈출시킴
    if flag == 0:  # flag가 0이면 소수
        return True
    else:
        return False


# rvs에 reverse한 결과로 만들고
rvs = []
for i in list:
    rvs.append(reverse(i))

# res에 소수인 것으로 만들고
res = []
for i in rvs:
    if isPrime(i):
        res.append(i)

for i in range(len(res)):  # 출력
    print(res[i], end=' ')
