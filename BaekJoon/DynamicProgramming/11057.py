import sys

THOUSAND = 1000
N = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(10)] for _ in range(THOUSAND + 1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:]) % 10007

print(sum(dp[N]) % 10007)
# 뒤에다 추가하는 원리, 근데 2차원으로
