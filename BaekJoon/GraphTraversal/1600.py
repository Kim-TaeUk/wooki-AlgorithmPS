import sys
from collections import deque

dx_horse = [-2, -1, 1, 2, 2, 1, -1, -2]
dy_horse = [1, 2, 2, 1, -1, -2, -2, -1]
dx_monkey = [-1, 0, 1, 0]
dy_monkey = [0, 1, 0, -1]


def bfs():
    global board, distance
    queue = deque()
    queue.append((0, 0, 0))
    distance[0][0][0] = 1

    while queue:
        current_x, current_y, jumped = queue.popleft()
        if current_x == H - 1 and current_y == W - 1:
            return distance[current_x][current_y][jumped] - 1

        if jumped < K:
            for i in range(8):
                next_x, next_y = current_x + dx_horse[i], current_y + dy_horse[i]
                if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:  # 격자판을 벗어난 경우
                    continue
                if board[next_x][next_y] == 1:  # 장애물인 경우
                    continue
                if distance[next_x][next_y][jumped + 1] != 0:  # 이미 갱신되어 있는 경우
                    continue
                distance[next_x][next_y][jumped + 1] = distance[current_x][current_y][jumped] + 1
                queue.append((next_x, next_y, jumped + 1))

        for i in range(4):
            next_x, next_y = current_x + dx_monkey[i], current_y + dy_monkey[i]
            if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:  # 격자판을 벗어난 경우
                continue
            if board[next_x][next_y] == 1:  # 장애물인 경우
                continue
            if distance[next_x][next_y][jumped] != 0:  # 이미 갱신되어 있는 경우
                continue
            distance[next_x][next_y][jumped] = distance[current_x][current_y][jumped] + 1
            queue.append((next_x, next_y, jumped))

    return -1


K = int(sys.stdin.readline().rstrip())
W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
distance = [[[0 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]
print(bfs())
