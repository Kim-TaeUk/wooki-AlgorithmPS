import sys
from collections import deque

dx = [-1, 0, 1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]


def bfs(start_x, start_y):
    global board, visited
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(8):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if board[next_x][next_y] == 1 and not visited[next_x][next_y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)
