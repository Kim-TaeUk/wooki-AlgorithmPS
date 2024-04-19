import sys

N, M = map(int, sys.stdin.readline().split())
lst = [i for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    lst[i], lst[j] = lst[j], lst[i]

print(*lst[1:])
