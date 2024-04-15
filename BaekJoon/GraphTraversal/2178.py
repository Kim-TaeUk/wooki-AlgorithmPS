import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append([start_x, start_y])

    visited[start_x][start_y] = True
    distance[start_x][start_y] = 1

    while queue:
        current_x, current_y = queue.popleft()
        if (current_x, current_y) == (end_x, end_y):
            return distance[current_x][current_y]

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            if visited[next_x][next_y]:
                continue
            if maze[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                distance[next_x][next_y] = distance[current_x][current_y] + 1
                queue.append([next_x, next_y])


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
distance = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, N - 1, M - 1))
