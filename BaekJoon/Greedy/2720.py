import sys

T = int(sys.stdin.readline().rstrip())
liam = [25, 10, 5, 1]
for _ in range(T):
    C = int(sys.stdin.readline().rstrip())
    res = []
    for x in liam:
        res.append(C // x)
        C %= x
    print(*res)
