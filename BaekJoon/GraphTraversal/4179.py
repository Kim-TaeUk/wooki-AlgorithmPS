from collections import deque
import sys


def bfs_fire():
    while queue_fire:
        current_x, current_y = queue_fire.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if (0 <= next_x < R and 0 <= next_y < C
                    and board[next_x][next_y] != '#' and fire_time[next_x][next_y] == -1):
                fire_time[next_x][next_y] = fire_time[current_x][current_y] + 1
                queue_fire.append([next_x, next_y])


def bfs_user():
    while queue_user:
        current_x, current_y = queue_user.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < R and 0 <= next_y < C:
                if (board[next_x][next_y] != '#' and user_time[next_x][next_y] == -1
                        and (fire_time[next_x][next_y] == -1
                             or fire_time[next_x][next_y] > user_time[current_x][current_y] + 1)):
                    user_time[next_x][next_y] = user_time[current_x][current_y] + 1
                    queue_user.append([next_x, next_y])
            else:
                print(user_time[current_x][current_y] + 1)
                exit()
    print('IMPOSSIBLE')


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
fire_time = [[-1 for _ in range(C)] for _ in range(R)]
user_time = [[-1 for _ in range(C)] for _ in range(R)]

queue_fire = deque()
queue_user = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            queue_fire.append([i, j])
            fire_time[i][j] = 0
        if board[i][j] == 'J':
            queue_user.append([i, j])
            user_time[i][j] = 0

dx = [-1, 0, 1, 0]  # 상하좌우 체크
dy = [0, 1, 0, -1]

bfs_fire()
bfs_user()
