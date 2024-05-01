import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def dfs(current_x, current_y, cnt):
    global board, res
    if current_x == 0 and current_y == C - 1 and cnt == K:
        res += 1
        return
    for i in range(4):
        next_x, next_y = current_x + dx[i], current_y + dy[i]
        if next_x < 0 or next_x >= R or next_y < 0 or next_y >= C:
            continue
        if board[next_x][next_y] == 'T':
            continue
        board[next_x][next_y] = 'T'  # 방문 표시
        dfs(next_x, next_y, cnt + 1)
        board[next_x][next_y] = '.'  # 상태 되돌리기


R, C, K = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
board[R - 1][0] = 'T'  # 시작 지점의 방문 표시를 꼭 하자!
dfs(R - 1, 0, 1)
print(res)
