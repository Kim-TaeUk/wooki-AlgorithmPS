import sys

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 범위 벗어났는지 확인하는 메서드
def OOB(a, b):
    return a < 0 or a >= N or b < 0 or b >= M


# x, y에서 direction 방향으로 마주치는 모든 빈 칸을 7로 바꾸는 메서드
# ex. (3, 1), direction 2(북) -> board2의 (2, 1), (1, 1), (0, 1)이 0 이면 모두 7로 변경
def upd(x, y, direction):
    direction %= 4
    while True:
        x += dx[direction]
        y += dy[direction]
        if OOB(x, y) or board2[x][y] == 6:
            return
        if board2[x][y] != 0:  # 해당 칸에 cctv가 있으면 통과니까 break가 아닌 continue
            continue
        board2[x][y] = 7


# 입력 및 초기 작업
N, M = map(int, sys.stdin.readline().split())
board1 = []  # 입력받은 배열 - 원본
cctv = []  # cctv의 좌표 담을 배열
mn = 0  # 사각 지대의 최소 크기(=답)
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board1.append(row)
    for j in range(M):
        if row[j] != 0 and row[j] != 6:
            cctv.append((i, j))  # cctv 찾으면 cctv 배열에 추가
        if row[j] == 0:
            mn += 1  # 문제에 cctv 1개 이상 조건 없으므로 아예 없는 것도 고려해야 하므로 빈칸의 개수로 설정하는 것이 안전

# cctv 방향 정하기 -> 4진법 활용
# cctv가 k개 -> tmp는 0 ~ 4^k - 1까지 돌아야 한다
"""
let, len(cctv) = 3

tmp: 0 ~ 63 (000 ~ 333)
brute: 0 ~ 63 (000 ~ 333)

cctv 배열에 있는 cctv 3개 중 하나를 고름
i: 0 ~ 2 

cctv 배열에서 고른 cctv의 좌표 
x, y = cctv[i]

direction = brute % 4
: 나머지 연산으로 tmp에서 추출한 각 cctv의 방향 구하기 (0 ~ 3)
-> 213(4)에서 3을 추출

brute //= 4
: 다음 cctv 방향 구하기 위해 전처리
-> 213(4)에서 3 추출했으니, 21(4)으로 남기기 위함
"""
for tmp in range(1 << (2 * len(cctv))):  # 1 << (2*cctv.size())는 4의 cctv.size()승
    # upd 메서드르 거치며 내부의 값이 계속 변경
    # 감시 영역에 걸리는 빈칸은 7로 바꾸는 작업을 할 배열
    board2 = [[elem for elem in row] for row in board1]

    brute = tmp
    for i in range(len(cctv)):
        direction = brute % 4
        brute //= 4
        x, y = cctv[i]
        if board1[x][y] == 1:
            upd(x, y, direction)
        elif board1[x][y] == 2:
            upd(x, y, direction)
            upd(x, y, direction + 2)
        elif board1[x][y] == 3:
            upd(x, y, direction)
            upd(x, y, direction + 1)
        elif board1[x][y] == 4:
            upd(x, y, direction)
            upd(x, y, direction + 1)
            upd(x, y, direction + 2)
        else:  # board1[x][y] == 5
            upd(x, y, direction)
            upd(x, y, direction + 1)
            upd(x, y, direction + 2)
            upd(x, y, direction + 3)

    val = 0
    for i in range(N):
        for j in range(M):
            val += (board2[i][j] == 0)
    mn = min(mn, val)

print(mn)
