import sys


def func(K, start):
    if K == M:
        print(" ".join(map(str, arr)))
        return

    tmp = 0
    for idx, x in lst[start - 1:]:
        if tmp != x:
            arr[K] = x
            tmp = arr[K]
            func(K + 1, idx + 1)


N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
lst = list(enumerate(lst))
arr = [0] * M
func(0, 1)
