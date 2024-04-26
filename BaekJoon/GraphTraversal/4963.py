import sys
from collections import deque

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]


def bfs(start_x, start_y):
    global board, visited, res
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(8):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w:
                continue
            if not visited[next_x][next_y] and board[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
    res += 1


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    res = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
    print(res)
