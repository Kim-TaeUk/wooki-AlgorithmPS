import sys

N = int(sys.stdin.readline().rstrip())
res = 0

for i in range(1, N):
    res += (N * i + i)

print(res)
