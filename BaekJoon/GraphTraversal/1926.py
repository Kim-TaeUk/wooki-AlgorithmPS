import sys


def bfs(start_x, start_y):
    # 필요한 변수 생성
    queue = []  # queue랑
    dx = [-1, 0, 1, 0]  # 상하좌우 체크
    dy = [0, 1, 0, -1]

    # queue에 시작 데이터 삽입하여 시작
    queue.append([start_x, start_y])

    # 단위 작업 - 방문 체크하고, 넓이 체크(+1)
    visited[start_x][start_y] = True
    area = 1

    while queue:  # queue에 데이터가 있는 동안
        current_x, current_y = queue.pop(0)  # queue에서 데이터 빼주고

        for i in range(4):  # 4방향 처리
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            # 4방향 처리한 next_x, next_y가 입력으로 주어진 범위 내 & 칠해진 곳일 때(1일 때) & 방문하지 않은 곳일 때만
            if 0 <= next_x < n and 0 <= next_y < m and painiting[next_x][next_y] == 1 and not visited[next_x][next_y]:
                # 단위 작업 - 방문 체크하고, 넓이 체크(+1)
                visited[next_x][next_y] = True
                area += 1
                # 그리고 queue에 삽입해주기까지
                queue.append([next_x, next_y])
    res.append(area)  # while문 종료 = 1개의 그림 종료


# 입력
n, m = map(int, sys.stdin.readline().split())
painiting = []
for _ in range(n):
    painiting.append(list(map(int, sys.stdin.readline().split())))

# 방문 체크 배열, 그림 개수, 그림 넓이 배열
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0
res = []

# bfs의 시작점이 될 수 있는 모든 점 찾기
for x in range(n):
    for y in range(m):
        if painiting[x][y] == 1 and not visited[x][y]:  # 그림이 칠해져 있고, 방문하지 않은 곳만 시작점 가능
            bfs(x, y)
            count += 1

print(count)
if res:
    print(max(res))
else:
    print(0)

