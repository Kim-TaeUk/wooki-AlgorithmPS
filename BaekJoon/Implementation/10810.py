import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0 for _ in range(N + 1)]
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i, j + 1):
        basket[x] = k

print(*basket[1:])
