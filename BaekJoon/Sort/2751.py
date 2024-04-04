import sys

N = int(sys.stdin.readline().rstrip())
N_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])
print(*N_list, sep="\n")
