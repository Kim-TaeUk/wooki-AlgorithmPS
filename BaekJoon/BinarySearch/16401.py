import sys

M, N = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(N_list)
res = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for x in N_list:
        cnt += x // mid
    if cnt >= M:
        res = mid
        left = mid + 1
    elif cnt < M:
        right = mid - 1

print(res)
