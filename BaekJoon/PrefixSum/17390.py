import sys

N, Q = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
prefix_sum = [0 for _ in range(N + 1)]
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + lst[i]
for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    print(prefix_sum[R] - prefix_sum[L - 1])
