import sys

N, K = map(int, sys.stdin.readline().split())
N_list = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
for x in reversed(N_list):
    if K >= x:
        cnt += K // x
        K %= x

print(cnt)
