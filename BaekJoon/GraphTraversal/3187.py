import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(start_x, start_y):
    global board, visited, wolf, sheep
    v, k = 0, 0
    if board[start_x][start_y] == 'v':
        v += 1
    if board[start_x][start_y] == 'k':
        k += 1
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= R or next_y < 0 or next_y >= C:
                continue
            if board[next_x][next_y] == '#':
                continue
            if visited[next_x][next_y]:
                continue
            if board[next_x][next_y] == 'v':
                v += 1
            if board[next_x][next_y] == 'k':
                k += 1
            queue.append((next_x, next_y))
            visited[next_x][next_y] = True

    if v >= k:
        wolf += v
    else:
        sheep += k


R, C = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and not visited[i][j]:
            bfs(i, j)

print(sheep, wolf)
