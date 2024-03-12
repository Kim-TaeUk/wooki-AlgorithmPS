import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, N + 1)]
for i in combinations_with_replacement(lst, M):
    print(" ".join(map(str, i)))
