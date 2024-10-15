import sys

N = int(sys.stdin.readline().rstrip())
lst = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])

res = 0
for i in range(1, N + 1):
    res = max(res, lst[N - i] * i)

print(res)
