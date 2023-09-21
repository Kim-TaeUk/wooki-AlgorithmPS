import sys

N = int(sys.stdin.readline())
N_list = []
for _ in range(N):
    N_list.append(int(sys.stdin.readline()))

N_list.sort()

for x in N_list:
    print(x)
