import sys

N = int(sys.stdin.readline().rstrip())
if N == 1:  # 1일 때 예외처리 안하면 IndexError 발생
    print(0)
    exit()
prime_num = []
for i in range(2, N + 1):
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime_num.append(i)

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
