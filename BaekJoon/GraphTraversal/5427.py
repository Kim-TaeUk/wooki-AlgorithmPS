import sys
from collections import deque


def bfs_fire(queue_fire):
    while queue_fire:
        current_x, current_y = queue_fire.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w:
                continue

            if fire_map[next_x][next_y] == -1 and board[next_x][next_y] != '#':
                fire_map[next_x][next_y] = fire_map[current_x][current_y] + 1
                queue_fire.append([next_x, next_y])


def bfs_man(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    distance[start_x][start_y] = 0

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < h and 0 <= next_y < w:
                if board[next_x][next_y] == '#':  # 벽이면 패스
                    continue
                # if (distance[current_x][current_y] > distance[next_x][next_y]
                #         and distance[next_x][next_y] != -1):  # 들어간 자리는 안들어가게
                #     continue
                if distance[next_x][next_y] >= 0:
                    continue
                if (fire_map[next_x][next_y] > distance[current_x][current_y] + 1) or (fire_map[next_x][next_y] == -1):
                    distance[next_x][next_y] = distance[current_x][current_y] + 1
                    queue.append([next_x, next_y])
            else:
                print(distance[current_x][current_y] + 1)
                return
    print('IMPOSSIBLE')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

    distance = [[-1 for _ in range(w)] for _ in range(h)]
    fire_map = [[-1 for _ in range(w)] for _ in range(h)]
    start_fire = deque()
    start = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                start_fire.append([i, j])
                fire_map[i][j] = 0
            if board[i][j] == '@':
                start.append([i, j])
    if len(start_fire) == 0:  # 불이 없을 때 고려
        fire_map = [[float('inf') for _ in range(w)] for _ in range(h)]
    else:
        bfs_fire(start_fire)
    bfs_man(start[0][0], start[0][1])
