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
    if k == 1:
        return False
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

# reverse()에서 list로 하나씩 분리한 다음 다시 꺼내서 10의 거듭제곱을 곱해줬는데
# sol 방식이 훨씬 깔끔하고 빠름.. -> reverse하는건 자주 나올 수 있으니 저대로 풀자 앞으로는

# isPrime()에서 1일 경우 예외처리 해야한다 -> 1은 소수가 아니니까!!
# isPrime()에서 for - else 구문 사용하면 flag 도입할 필요가 없음 -> 배웠으면 사용하자!
# isPrime()에서 절반까지만 나눠보면 된다 -> 실행속도 줄이기..!

# 결과 출력할 때 굳이 list에 다시 넣지 말고, isPrime의 return이 boolean이니까
# 조건문 만족하면 바로바로 뽑으면 된다 -> 2번 일 하지 말자
