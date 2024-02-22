import sys
from collections import deque


def find_se(L, R, C):
    cnt = 0
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if cnt == 2:
                    return
                if building[i][j][k] == 'S':
                    distance[i][j][k] = 0
                    queue.append([i, j, k])
                    cnt += 1
                if building[i][j][k] == 'E':
                    end_list.append([i, j, k])
                    cnt += 1


def bfs():
    while queue:
        current_z, current_x, current_y = queue.popleft()

        for i in range(6):
            next_z, next_x, next_y = current_z + dz[i], current_x + dx[i], current_y + dy[i]
            if next_z == end_list[0][0] and next_x == end_list[0][1] and next_y == end_list[0][2]:
                print("Escaped in", distance[current_z][current_x][current_y] + 1, "minute(s).")
                return
            if next_z < 0 or next_z >= L or next_x < 0 or next_x >= R or next_y < 0 or next_y >= C:
                continue
            if distance[next_z][next_x][next_y] > 0:
                continue
            if distance[next_z][next_x][next_y] < 0:
                if building[next_z][next_x][next_y] == '#':
                    continue
                queue.append([next_z, next_x, next_y])
                distance[next_z][next_x][next_y] = distance[current_z][current_x][current_y] + 1
    print("Trapped!")


while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = [[] * R for _ in range(L)]
    for i in range(L):
        for _ in range(R):
            building[i].append(list(map(str, sys.stdin.readline().rstrip())))
        sys.stdin.readline()
    queue = deque()
    end_list = deque()
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    distance = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    find_se(L, R, C)
    bfs()
