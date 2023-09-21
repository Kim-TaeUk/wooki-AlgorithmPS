import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for x in M_list:
    if x in N_list:
        print(1)
    else:
        print(0)

# 시간 초과 - 시간복잡도 O(MN)
