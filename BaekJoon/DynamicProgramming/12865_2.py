import sys

N, K = map(int, sys.stdin.readline().split())
bag = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0 for _ in range(K + 1)]

for i in range(1, N + 1):
    weight, value = bag[i - 1]
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j - weight] + value, dp[j])

print(dp[K])
