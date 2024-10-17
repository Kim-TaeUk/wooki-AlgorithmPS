import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    X = list(map(int, sys.stdin.readline().split()))

    tmp = X[0]
    res = X[0]
    for i in range(1, N):
        tmp = max(tmp + X[i], X[i])
        res = max(tmp, res)

    print(res)

# Kadane's Algorithm -> O(N)
