import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global board, distance
    queue = deque()
    queue.append([0, 0, 0])
    distance[0][0][0] = 1

    while queue:
        current_x, current_y, crashed = queue.popleft()
        if current_x == N - 1 and current_y == M - 1:
            return distance[current_x][current_y][crashed]

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if distance[next_x][next_y][crashed] != 0:  # 방문한 곳 제외
                continue

            # next_x, next_y가 벽 & 벽 파괴 가능
            if board[next_x][next_y] == 1 and crashed == 0:
                distance[next_x][next_y][1] = distance[current_x][current_y][crashed] + 1
                queue.append([next_x, next_y, 1])

            # next_x, next_y가 벽X
            if board[next_x][next_y] == 0:
                distance[next_x][next_y][crashed] = distance[current_x][current_y][crashed] + 1
                queue.append([next_x, next_y, crashed])
    return -1


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
distance = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
print(bfs())
