import sys


def func(K, start):
    if K == 6:
        print(" ".join(map(str, arr)))
        return

    for idx, x in S[start - 1:]:
        if not is_used[idx]:
            is_used[idx] = True
            arr[K] = x
            func(K + 1, idx + 1)
            is_used[idx] = False


while True:
    lst = list(map(int, sys.stdin.readline().split()))
    N = lst[0]
    S = list(enumerate(lst[1:]))

    if N == 0:
        exit(0)

    arr = [0] * 6
    is_used = [False] * (N + 1)
    func(0, 1)
    print()
