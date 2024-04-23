import sys

N = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(2)] for _ in range(90 + 1)]
dp[1] = [0, 1]
for i in range(2, N + 1):
    dp[i][0] = sum(dp[i - 1])
    dp[i][1] = dp[i - 1][0]

print(sum(dp[N]))
