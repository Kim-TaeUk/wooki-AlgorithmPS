def print_arr(_arr):
    for row in _arr:
        print(row)
    print()


def rotate_clockwise_90(arr):  # 시계 방향 90도 회전
    N, M = len(arr), len(arr[0])  # 3, 5
    res = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            res[j][N - i - 1] = arr[i][j]
    return res


def rotate_clockwise_180(arr):  # 시계 방향 180도 회전
    N, M = len(arr), len(arr[0])
    res = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            res[N - i - 1][M - j - 1] = arr[i][j]
    return res


def rotate_clockwise_270(arr):  # 시계 방향 270도 회전
    N, M = len(arr), len(arr[0])
    res = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            res[M - j - 1][i] = arr[i][j]
    return res


# 3*5 배열 arr
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15]]

print_arr(rotate_clockwise_90(arr))
print_arr(rotate_clockwise_180(arr))
print_arr(rotate_clockwise_270(arr))
