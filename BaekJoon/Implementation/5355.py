import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    lst = list(map(str, sys.stdin.readline().split()))
    res = float(lst.pop(0))

    for x in lst:
        if x == "@":
            res *= 3
        elif x == "%":
            res += 5
        elif x == "#":
            res -= 7

    print('{:0.2f}'.format(res))
