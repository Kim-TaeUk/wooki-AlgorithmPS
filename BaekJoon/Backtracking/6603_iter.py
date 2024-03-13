import sys
from itertools import combinations

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    K = lst[0]
    S = lst[1:]
    if K == 0:
        exit(0)

    for i in combinations(S, 6):
        print(" ".join(map(str, i)))
    print()
