import sys

N = int(sys.stdin.readline().rstrip())
res = 1

if N > 0:
    for x in range(1, N + 1):
        res *= x

print(res)
