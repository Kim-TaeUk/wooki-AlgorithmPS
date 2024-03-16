import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N + 1)
dp[0] = -1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])

while N != 0:
    print(N, end=" ")
    if dp[N] == dp[N - 1] + 1:
        N -= 1
    elif N % 2 == 0 and dp[N] == dp[N // 2] + 1:
        N //= 2
    elif N % 3 == 0 and dp[N] == dp[N // 3] + 1:
        N //= 3
