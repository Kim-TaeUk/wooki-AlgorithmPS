import sys

N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(33334)]
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] * 3) % 1000000009

print(dp[N])
