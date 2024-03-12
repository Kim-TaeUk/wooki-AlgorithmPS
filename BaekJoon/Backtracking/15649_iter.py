import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, N + 1)]

for i in permutations(lst, M):
    print(" ".join(map(str, i)))
