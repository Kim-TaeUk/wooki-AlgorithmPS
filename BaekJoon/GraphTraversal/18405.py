import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global board, virus
    queue = deque(virus)

    while queue:
        virus_num, current_x, current_y, time = queue.popleft()
        if time == S:
            break
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if board[next_x][next_y] == 0:
                board[next_x][next_y] = virus_num
                queue.append((virus_num, next_x, next_y, time + 1))


N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())
virus = []

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus.append((board[i][j], i, j, 0))
virus.sort()
bfs()
print(board[X - 1][Y - 1])
