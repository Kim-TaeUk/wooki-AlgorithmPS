import sys
from collections import deque


def bfs():
    queue = deque()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if board[i][j][k] == 1:
                    queue.append([i, j, k])
                if board[i][j][k] == 0:  # 안익은 토마토 -1
                    distance[i][j][k] = -1

    while queue:
        current_h, current_x, current_y = queue.popleft()

        for i in range(6):
            next_h, next_x, next_y = current_h + dh[i], current_x + dx[i], current_y + dy[i]
            if next_h < 0 or next_h >= H or next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if distance[next_h][next_x][next_y] >= 0:
                continue
            distance[next_h][next_x][next_y] = distance[current_h][current_x][current_y] + 1
            queue.append([next_h, next_x, next_y])


def find_max():
    max_value = float('-inf')

    for height in distance:
        for row in height:
            for element in row:
                if element == -1:
                    return -1
                if element > max_value:
                    max_value = element
    return max_value


M, N, H = map(int, sys.stdin.readline().split())
board = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
distance = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
bfs()
print(find_max())
