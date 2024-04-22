import sys

THOUSAND = 1000

N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(THOUSAND + 1)]
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[N] % 10007)
