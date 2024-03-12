import sys


def func(K):
    if K == M:
        print(" ".join(map(str, arr)))
        return

    tmp = 0
    for x in lst:
        if tmp != x:
            arr[K] = x
            tmp = arr[K]
            func(K + 1)


N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
arr = [0] * M
func(0)
