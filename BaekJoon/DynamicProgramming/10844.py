import sys

THOUSAND = 1000
TEN_BILLION = 1000000000
N = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(10)] for _ in range(THOUSAND + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1] % TEN_BILLION
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % TEN_BILLION

print(sum(dp[N]) % TEN_BILLION)
