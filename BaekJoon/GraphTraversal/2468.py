import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(start_x, start_y, h):
    global board, visited
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if board[next_x][next_y] <= h or visited[next_x][next_y]:
                continue
            queue.append((next_x, next_y))
            visited[next_x][next_y] = True


N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_height = max(map(max, board))

res = 0
for height in range(max_height):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > height:
                bfs(i, j, height)
                cnt += 1
    res = max(res, cnt)

print(res)
