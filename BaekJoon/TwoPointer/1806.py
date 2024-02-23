import sys

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

sum = lst[0]
rt = 0
res = float('inf')
for lt in range(N):
    while rt < N and sum < S:
        rt += 1
        if rt < N:
            sum += lst[rt]

    if rt == N:
        break

    res = min(res, rt - lt + 1)
    sum -= lst[lt]

if res == float('inf'):
    res = 0

print(res)
