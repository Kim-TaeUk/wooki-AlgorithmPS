import sys

dp = [0 for _ in range(100000 + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6
for i in range(7, 100000 + 1):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(dp[N] % 1000000009)
