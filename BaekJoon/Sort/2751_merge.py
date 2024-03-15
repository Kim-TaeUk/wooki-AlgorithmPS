import sys


def merge(start, end):
    tmp = []
    mid = (start + end) // 2
    left_idx = start
    right_idx = mid

    for _ in range(end - start):
        if right_idx == end:
            tmp.append(arr[left_idx])
            left_idx += 1
        elif left_idx == mid:
            tmp.append(arr[right_idx])
            right_idx += 1
        elif arr[left_idx] <= arr[right_idx]:
            tmp.append(arr[left_idx])
            left_idx += 1
        else:
            tmp.append(arr[right_idx])
            right_idx += 1

    for i in range(start, end):
        arr[i] = tmp[i - start]


def merge_sort(start, end):
    if start + 1 == end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

merge_sort(0, N)
print(*arr)
