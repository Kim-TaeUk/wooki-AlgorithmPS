# Quick Sort
# Divide and Conquer + Recursive
# 평균 O(NlogN), 최악 O(N^2)
# stable 하지 않음


# arr[start:end - 1]을 정렬
def quick_sort(start, end):
    # base condition
    if start + 1 >= end:
        return

    pivot = arr[0]
    left = start + 1
    right = end - 1

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    quick_sort(start, right)
    quick_sort(right + 1, end)


arr = [6, -8, 1, 12, 8, 3, 7, -7]
N = len(arr)
quick_sort(0, N)
print(arr)
