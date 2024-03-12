import sys


def func(K):
    global is_used
    if K == M:
        print(" ".join(map(str, arr)))
        return

    for x in lst:
        if not is_used[x]:
            arr[K] = x
            is_used[x] = True
            func(K + 1)
            is_used[x] = False


N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
arr = [0] * M
is_used = [False] * (max(lst) + 1)
func(0)

# 그냥 lst의 최대만큼 is_used 만들어서 쓰기
