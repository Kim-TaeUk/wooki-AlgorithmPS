from collections import deque
import sys


def bfs():
    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if distance[next_x][next_y] >= 0:
                continue
            distance[next_x][next_y] = distance[current_x][current_y] + 1
            queue.append([next_x, next_y])


def find_max():
    has_zero = False
    max_value = float('-inf')

    for row in distance:
        for element in row:
            if element == -1:
                has_zero = True
                break
            if element > max_value:
                max_value = element

    if has_zero:
        print(-1)
    else:
        print(max_value)


M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
distance = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])
        if box[i][j] == 0:
            distance[i][j] = -1
bfs()
find_max()
