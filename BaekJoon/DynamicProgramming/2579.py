import sys

N = int(sys.stdin.readline().rstrip())
scores = [0]
for _ in range(N):
    scores.append(int(sys.stdin.readline().rstrip()))

if N == 1:
    print(scores[1])
    exit()

dp = [[0, 0, 0] for _ in range(N + 3)]
dp[1][1] = scores[1]
dp[1][2] = 0
dp[2][1] = scores[2]
dp[2][2] = scores[1] + scores[2]

for i in range(3, N + 1):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + scores[i]
    dp[i][2] = dp[i - 1][1] + scores[i]

print(max(dp[N][1], dp[N][2]))
