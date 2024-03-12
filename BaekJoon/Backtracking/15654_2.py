import sys


def func(K):
    global is_used
    if K == M:
        print(" ".join(map(str, arr)))
        return

    for idx, x in lst:
        if not is_used[idx]:
            arr[K] = x
            is_used[idx] = True
            func(K + 1)
            is_used[idx] = False


N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
lst = list(enumerate(lst))
arr = [0] * M
is_used = [False] * (N + 1)
func(0)

# enumerate로 lst 가공해서 쓰기
