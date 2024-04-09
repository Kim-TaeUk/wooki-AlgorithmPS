import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 번호별 회전 방향 - lookup table
cctv = [[], [0], [0, 2], [0, 1], [0, 1, 3], [0, 1, 2, 3]]


# CCTV가 있는 좌표 구하기
def get_cctv():
    global board, cctv_list
    for i in range(N):
        for j in range(M):
            if board[i][j] in cctv_num:
                cctv_list.append([i, j])


def calculate(temp_list):
    visited = [[0 for _ in range(M)] for _ in range(N)]

    # 모든 CCTV에 대해서 처리: 좌표(start_x, start_y), 회전 방향(rotate), CCTV 번호(cctv_type)
    for i in range(CNT):  # CCTV_list에서 CCTV가 있는 좌표,
        start_x, start_y = cctv_list[i]  # 0 ~ N-1, 0 ~ M-1
        rotate = temp_list[i]  # 0 ~ 3
        cctv_type = board[start_x][start_y]  # 1 ~ 5

        # type에 따라 모든 방향을 뻗어가기 + visited에 방문 처리
        for direction in cctv[cctv_type]:  # type에 따라 방향 결정
            direction = (direction + rotate) % 4  # 회전 처리(방향 조정)
            current_x, current_y = start_x, start_y

            while True:  # 뻗어나가기
                current_x, current_y = current_x + dx[direction], current_y + dy[direction]
                if current_x < 0 or current_x >= N or current_y < 0 or current_y >= M:
                    break
                if board[current_x][current_y] == 6:  # 벽이면 그만 뻗어가기
                    break
                visited[current_x][current_y] = 1

    # 사각지대 (0이고(빈칸), 미방문) 개수 카운트
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    return cnt


def func(n, temp_list):
    global ans
    if n == CNT:  # 모든 CCTV의 방향 정하기 완료
        ans = min(ans, calculate(temp_list))
        return

    func(n + 1, temp_list + [0])  # 0도 회전
    func(n + 1, temp_list + [1])  # 90도 회전
    func(n + 1, temp_list + [2])  # 180도 회전
    func(n + 1, temp_list + [3])  # 270도 회전


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv_num = [1, 2, 3, 4, 5]
cctv_list = []
get_cctv()
CNT = len(cctv_list)
ans = N * M  # 최대 개수로 초기값 줘놓기
func(0, [])
print(ans)
