from collections import deque
import sys


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    board[start_x][start_y] = 0

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < M and 0 <= next_y < N and board[next_x][next_y] == 1:
                queue.append([next_x, next_y])
                board[next_x][next_y] = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        board[X][Y] = 1

    res = 0
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                bfs(i, j)
                res += 1
    print(res)
