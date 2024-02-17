from collections import deque
import sys


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True
    count = 0

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y] and campus[next_x][next_y] != 'X':
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])
                if campus[next_x][next_y] == 'P':
                    count += 1
    return count


N, M = map(int, sys.stdin.readline().split())
campus = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            count = bfs(i, j)

if count == 0:
    print('TT')
else:
    print(count)
