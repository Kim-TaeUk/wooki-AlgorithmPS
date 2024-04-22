import sys

N = int(sys.stdin.readline().rstrip())
dp = [1 for _ in range(10)]
for _ in range(N - 1):
    for j in range(1, 10):
        dp[j] = dp[j] + dp[j - 1]

print(sum(dp) % 10007)
# 앞에다 추가하는 원리
