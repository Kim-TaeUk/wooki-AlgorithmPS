import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(r, c):
    global board, distance
    distance[r][c] = 0
    queue = deque()
    queue.append((r, c))

    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= 5 or next_y < 0 or next_y >= 5:
                continue
            if board[next_x][next_y] == -1:
                continue
            if distance[next_x][next_y] == -1:
                if board[next_x][next_y] == 1:
                    return distance[current_x][current_y] + 1
                distance[next_x][next_y] = distance[current_x][current_y] + 1
                queue.append((next_x, next_y))
    return -1


board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
distance = [[-1 for _ in range(5)] for _ in range(5)]
r, c = map(int, sys.stdin.readline().split())
print(bfs(r, c))
