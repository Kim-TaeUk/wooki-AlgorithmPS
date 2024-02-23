import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()
res = float('inf')
rt = 0
for lt in range(N):
    while rt < N and lst[rt] - lst[lt] < M:
        rt += 1
    if rt == N:
        break
    res = min(res, lst[rt] - lst[lt])
print(res)
