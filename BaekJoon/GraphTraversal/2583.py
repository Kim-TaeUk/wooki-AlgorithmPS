import sys
from collections import deque


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    board[start_x][start_y] = 1
    area = 1

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and board[next_x][next_y] == 0:
                board[next_x][next_y] = 1
                queue.append([next_x, next_y])
                area += 1
    return area


M, N, K = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = -1
res = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            res.append(bfs(i, j))

print(len(res))
res.sort()
print(*res)
