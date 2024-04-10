import sys


def can_attach(x, y):  # 노트북에 스티커 붙일 수 있는지 확인
    global notebook, sticker
    for i in range(R):
        for j in range(C):
            if 0 > i + x or i + x >= N or 0 > j + y or j + y >= M:  # 스티커가 노트북 범위를 벗어날 때
                return False
            if sticker[i][j] == 1 and notebook[i + x][j + y] == 1:  # 붙이려는 스티커와 노트북에 붙어있는 스티커가 겹칠 때
                return False
    return True


def attach(x, y):  # 노트북에 스티커 붙이기
    global notebook
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                notebook[i + x][j + y] = 1


def process_sticker():
    global sticker, is_pasted
    for i in range(N):
        for j in range(M):
            if can_attach(i, j):
                attach(i, j)
                is_pasted = True
                return


def rotate():  # 시계 방향으로 90도 회전시키기
    global sticker, R, C
    sticker = [list(row) for row in zip(*sticker[::-1])]
    R, C = C, R  # 꼭 바꿔줘야 함...!


def get_answer():
    global notebook
    res = 0
    for i in range(N):
        for j in range(M):
            if notebook[i][j] == 1:
                res += 1
    return res


N, M, K = map(int, sys.stdin.readline().split())
notebook = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    for i in range(4):
        is_pasted = False
        process_sticker()  # 지금 회전 상태에서 스티커 붙일 수 있는지 확인
        if is_pasted:
            break
        rotate()  # 90도 회전시키기

print(get_answer())
