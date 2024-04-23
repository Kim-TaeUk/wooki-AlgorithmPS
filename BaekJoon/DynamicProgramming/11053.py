import sys

THOUSAND = 1000

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(THOUSAND + 1)]

dp[0] = 1
for i in range(1, N):
    mx = 0
    for j in range(0, i):
        if lst[i] > lst[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1

print(max(dp))
