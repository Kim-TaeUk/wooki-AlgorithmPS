from collections import deque
import sys


def bfs():
    # 시작점이 될 수 있는 좌표가 모두 queue에 들어가 있는 상태로 bfs 시작!
    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and box[next_x][next_y] == 0:
                box[next_x][next_y] = box[current_x][current_y] + 1
                queue.append([next_x, next_y])


def find_max():
    has_zero = False
    max_value = float('-inf')

    for row in box:
        for element in row:
            if element == 0:
                has_zero = True
                break
            if element > max_value:
                max_value = element

    if has_zero:
        print(-1)
    else:
        print(max_value - 1)


# 입력
M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 필요한 변수 생성
queue = deque()  # queue랑
dx = [-1, 0, 1, 0]  # 상하좌우 체크
dy = [0, 1, 0, -1]

# 시작점이 여러개이기 때문에, 순회하면서 시작점이 되는 것들을 모두 queue에 넣기!
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()
find_max()
