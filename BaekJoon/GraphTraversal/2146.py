import sys
from collections import deque


# 섬 구분
def make_label(start_x, start_y, label):
    queue = deque()
    queue.append([start_x, start_y])
    visited = [[False for _ in range(N)] for _ in range(N)]
    board[start_x][start_y] = label
    visited[start_x][start_y] = True

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue

            if not visited[next_x][next_y]:
                if board[next_x][next_y] == 1:
                    board[next_x][next_y] = label
                    queue.append([next_x, next_y])
                    visited[next_x][next_y] = True


def bfs(start_x, start_y):
    queue = deque()
    distance = [[-1 for _ in range(N)] for _ in range(N)]
    label = board[start_x][start_y]

    # 해당 bfs에 포함되는 섬의 좌표는 모두 queue에 넣고 시작
    for i in range(N):
        for j in range(N):
            if board[i][j] == label:
                is_surrounded = True
                distance[i][j] = 0
                _visited[i][j] = True  # 71번째 줄에서 bfs 중복으로 안하기 위해
                for k in range(4):  # 경계점만 queue에 넣기
                    next_i, next_j = i + dx[k], j + dy[k]
                    if 0 <= next_i < N and 0 <= next_j < N:
                        if board[next_i][next_j] != label:
                            is_surrounded = False
                            queue.append([i, j])
                            break
                if is_surrounded:
                    continue

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue

            if distance[next_x][next_y] == -1:
                if board[next_x][next_y] == 0:  # 바다일 때
                    distance[next_x][next_y] = distance[current_x][current_y] + 1
                    queue.append([next_x, next_y])
                else:  # 다른 섬일 때
                    return distance[current_x][current_y]


N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
_visited = [[False for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

label = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            make_label(i, j, label)
            label += 1

res = float('inf')
for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and not _visited[i][j]:
            res = min(res, bfs(i, j))

print(res)
