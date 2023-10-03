import sys

N, M = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
prefixsum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        prefixsum[i + 1][j + 1] = (prefixsum[i + 1][j]
                                   + prefixsum[i][j + 1]
                                   - prefixsum[i][j]
                                   + numbers[i][j])

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    regionsum = (prefixsum[x2][y2]
                 - prefixsum[x1 - 1][y2]
                 - prefixsum[x2][y1 - 1]
                 + prefixsum[x1 - 1][y1 - 1])
    print(regionsum)
