import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(M):
        current_x, current_y = i, j
        # 가는 길이 아닐 때
        if dp[current_x][current_y] == 0:
            continue
        for k in range(4):
            next_x, next_y = current_x + dx[k], current_y + dy[k]
            # board 나가려고 할 때
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            # 내리막길이 아닐 때
            if board[current_x][current_y] <= board[next_x][next_y]:
                continue
            dp[next_x][next_y] += dp[current_x][current_y]

print(dp[N - 1][M - 1])
