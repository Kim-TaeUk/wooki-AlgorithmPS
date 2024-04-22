import sys

N = int(sys.stdin.readline().rstrip())
dp = [1 for _ in range(10)]
for i in range(N - 1):
    for j in range(10):
        dp[j] = sum(dp[j:])

print(sum(dp) % 10007)
# 뒤에다 추가하는 원리, 근데 1차원으로
