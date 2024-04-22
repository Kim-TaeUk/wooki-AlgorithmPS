import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = board[0][0]

for i in range(1, N):
    dp[i][0] += dp[i - 1][0] + board[i][0]
for j in range(1, M):
    dp[0][j] += dp[0][j - 1] + board[0][j]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + board[i][j]

print(dp[N - 1][M - 1])
