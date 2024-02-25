import sys


# 에라토스테네스의 체 이용
def get_prime(n):
    arr = [True for _ in range(n + 1)]
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    return [num for num, is_Prime in enumerate(arr) if is_Prime]


N = int(sys.stdin.readline().rstrip())
if N == 1:  # 1일 때 예외처리 안하면 IndexError 발생
    print(0)
    exit()
prime_num = get_prime(N + 1)

res = 0
rt = 0
sum = prime_num[0]

for lt in range(len(prime_num)):
    while sum < N and rt < len(prime_num) - 1:
        rt += 1
        sum += prime_num[rt]
    if sum == N:
        res += 1
    sum -= prime_num[lt]

print(res)
