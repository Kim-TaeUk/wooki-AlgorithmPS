import sys

# sys.setrecursionlimit(10 ** 6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(current_x, current_y):
    if dp[current_x][current_y] == -1:  # 아직 계산 안 한 곳(=첫 방문하는 곳)
        dp[current_x][current_y] = 0
        for k in range(4):  # 4방향
            previous_x, previous_y = current_x + dx[k], current_y + dy[k]  # 이전 좌표 계산
            if previous_x < 0 or previous_x >= N or previous_y < 0 or previous_y >= M:  # 범위 체크
                continue
            if board[previous_x][previous_y] > board[current_x][current_y]:  # 내리막길인 경우만
                dp[current_x][current_y] += dfs(previous_x, previous_y)  # 경로 누적
    return dp[current_x][current_y]


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1

print(dfs(N - 1, M - 1))
