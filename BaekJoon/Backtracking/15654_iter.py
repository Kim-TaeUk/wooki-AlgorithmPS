import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
for i in permutations(lst, M):
    print(" ".join(map(str, i)))
