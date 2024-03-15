import sys

N, M = map(int, sys.stdin.readline().split())
lst_A = list(map(int, sys.stdin.readline().split()))
lst_B = list(map(int, sys.stdin.readline().split()))
lst = []

idx_A, idx_B = 0, 0
for _ in range(N + M):
    if idx_B == M:
        lst.append(lst_A[idx_A])
        idx_A += 1
    elif idx_A == N:
        lst.append(lst_B[idx_B])
        idx_B += 1
    elif lst_A[idx_A] <= lst_B[idx_B]:
        lst.append(lst_A[idx_A])
        idx_A += 1
    else:
        lst.append(lst_B[idx_B])
        idx_B += 1

print(*lst)
