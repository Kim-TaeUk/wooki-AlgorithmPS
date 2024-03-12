import sys


def func(K):
    if K == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(N):
        arr[K] = lst[i]
        func(K + 1)


N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
arr = [0] * M
func(0)
