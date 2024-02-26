import sys

N, K = map(int, sys.stdin.readline().split())
lst = [[i, 0, 0] for i in range(7)]
for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    if S == 0:
        lst[Y][1] += 1
    if S == 1:
        lst[Y][2] += 1

res = 0
for i in range(1, 7):
    for j in range(1, 3):
        if lst[i][j] % K == 0:
            res += lst[i][j] // K
        else:
            res += lst[i][j] // K + 1

print(res)
