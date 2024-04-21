import sys

N, A, B = map(int, sys.stdin.readline().split())
res = 0

while True:
    if A == B:
        print(res)
        break
    A -= A // 2
    B -= B // 2
    res += 1
