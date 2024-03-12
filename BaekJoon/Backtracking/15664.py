import sys


def func(K, start):
    global is_used
    if K == M:
        print(" ".join(map(str, arr)))
        return

    tmp = 0
    for idx, x in lst[start - 1:]:
        if not is_used[idx] and tmp != x:
            is_used[idx] = True
            arr[K] = x
            tmp = arr[K]
            func(K + 1, idx + 1)
            is_used[idx] = False


N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
lst = list(enumerate(lst))
arr = [0] * M
is_used = [False] * (N + 1)
func(0, 1)
