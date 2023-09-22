import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

count = Counter(N_list)

for x in M_list:
    if x in count:
        print(count[x], end=" ")
    else:
        print(0, end=" ")

# 내장 모듈 Counter 사용
