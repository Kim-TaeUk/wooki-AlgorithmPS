import sys

n = int(sys.stdin.readline().strip())

if n == 2:
    A, B = map(int, sys.stdin.readline().split())
    for x in range(1, min(A, B) + 1):
        if A % x == 0 and B % x == 0:
            print(x)


else:
    A, B, C = map(int, sys.stdin.readline().split())
    for x in range(1, min(A, B, C) + 1):
        if A % x == 0 and B % x == 0 and C % x == 0:
            print(x)

# Python3 - 시간초과
# PyPy3 - 통과
