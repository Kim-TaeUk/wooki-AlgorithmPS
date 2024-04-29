import sys

N = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(3)] for _ in range(N + 1)]

dp[0][0] = 1
dp[0][1] = 0
dp[0][2] = 3
for i in range(1, N + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][2] - dp[i][0]
    dp[i][2] = (3 * dp[i][0] + 2 * dp[i][1]) % 9901

print(dp[N - 1][2] % 9901)
