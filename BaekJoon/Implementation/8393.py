import sys

n = int(sys.stdin.readline().rstrip())
res = 0
for x in range(1, n + 1):
    res += x
print(res)
