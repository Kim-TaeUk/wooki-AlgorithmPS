from collections import deque
import sys


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True
    count = 1

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and board[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])
                count += 1
    return count


N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            res.append(bfs(i, j))

res.sort()
print(len(res))
for x in res:
    print(x)
