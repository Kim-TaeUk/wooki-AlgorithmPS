import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dct = dict()
    for _ in range(N):
        name, types = map(str, sys.stdin.readline().split())
        if types in dct:
            dct[types] += 1
        else:
            dct[types] = 1

    res = 1
    for value in dct.values():
        res *= (value + 1)
    print(res - 1)
