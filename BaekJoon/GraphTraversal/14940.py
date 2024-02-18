from collections import deque
import sys


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    res[start_x][start_y] = 0
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                if board[next_x][next_y] == 0:
                    res[next_x][next_y] = 0
                if board[next_x][next_y] == 1:
                    res[next_x][next_y] = res[current_x][current_y] + 1
                    queue.append([next_x, next_y])


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
res = [[-1] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if board[i][j] == 2:
                bfs(i, j)
            if board[i][j] == 0:
                res[i][j] = 0
                visited[i][j] = True

for row in res:
    for x in row:
        print(x, end=' ')
    print()
