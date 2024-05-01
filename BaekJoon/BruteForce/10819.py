import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
res = 0
for arr in permutations(lst):
    tmp = sum([abs(arr[i] - arr[i - 1]) for i in range(1, N)])
    res = max(tmp, res)

print(res)
