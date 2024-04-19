import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    zero, one = 1, 0
    for _ in range(N):
        zero, one = one, zero + one
    print(zero, one)
