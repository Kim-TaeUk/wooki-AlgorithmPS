from collections import deque
import sys


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()
        color = board[start_x][start_y]

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                if color == board[next_x][next_y]:
                    queue.append([next_x, next_y])
                    visited[next_x][next_y] = True


def bfs_weak(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()
        color = board[current_x][current_y]

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                if color == 'R' or color == 'G':
                    if board[next_x][next_y] == 'R' or board[next_x][next_y] == 'G':
                        queue.append([next_x, next_y])
                        visited[next_x][next_y] = True
                if color == board[next_x][next_y]:
                    queue.append([next_x, next_y])
                    visited[next_x][next_y] = True


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

visited = [[False] * N for _ in range(N)]
res_normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            res_normal += 1
print(res_normal)

visited = [[False] * N for _ in range(N)]
res_weak = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_weak(i, j)
            res_weak += 1
print(res_weak)
