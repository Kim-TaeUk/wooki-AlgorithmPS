import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    lst = []
    for _ in range(N):
        S, L = map(str, sys.stdin.readline().split())
        lst.append((S, int(L)))

    lst.sort(key=lambda x: -x[1])
    print(lst[0][0])
