import sys


def binary_search(value):
    global lst
    left = 0  # index
    right = N - 1  # index
    res = -1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == value:
            res = mid
            right = mid - 1
        elif lst[mid] < value:
            left = mid + 1
        elif lst[mid] > value:
            right = mid - 1
    return res


N, M = map(int, sys.stdin.readline().split())
lst = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])
for _ in range(M):
    print(binary_search(int(sys.stdin.readline().rstrip())))
