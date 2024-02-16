import sys


def bfs(start_x, start_y, end_x, end_y):
    # 필요한 변수 생성
    queue = []  # queue랑
    dx = [-1, 0, 1, 0]  # 상하좌우 체크
    dy = [0, 1, 0, -1]

    # queue에 시작 데이터 삽입하여 시작
    queue.append([start_x, start_y])

    # 단위 작업 - 방문 체크하고, 길이 기록(이전 좌표에서 +1)
    visited[start_x][start_y] = True
    distance[start_x][start_y] = 1

    while queue:  # queue에 데이터가 있는 동안
        current_x, current_y = queue.pop(0)  # queue에서 데이터 빼주고
        if (current_x, current_y) == (end_x, end_y):  # 도착지 좌표면 종료!
            return distance[current_x][current_y]

        for i in range(4):  # 4방향 처리
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < M and maze[next_x][next_y] == 1 and not visited[next_x][next_y]:
                # 단위 작업 - 방문 체크하고, 길이 기록(이전 좌표에서 +1)
                visited[next_x][next_y] = True
                distance[next_x][next_y] = distance[current_x][current_y] + 1
                # 그리고 queue에 삽입해주기까지
                queue.append([next_x, next_y])


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
distance = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, N - 1, M - 1))
