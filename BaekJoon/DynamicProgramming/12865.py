import sys

N, K = map(int, sys.stdin.readline().split())
bag = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = bag[i - 1]
    for j in range(1, K + 1):
        if j >= weight:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
