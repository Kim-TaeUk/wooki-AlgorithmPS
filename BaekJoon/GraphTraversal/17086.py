import sys
from collections import deque


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(8):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                if board[next_x][next_y] != 1:
                    if board[next_x][next_y] == 0 or board[next_x][next_y] > board[current_x][current_y] + 1:
                        visited[next_x][next_y] = True
                        queue.append([next_x, next_y])
                        board[next_x][next_y] = board[current_x][current_y] + 1


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            visited = [[False for _ in range(M)] for _ in range(N)]
            bfs(i, j)

res = float('-inf')
for row in board:
    for element in row:
        res = max(res, element)

print(res - 1)
