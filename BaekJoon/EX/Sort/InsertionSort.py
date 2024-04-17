# Insertion Sort
# O(N^2)

arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
N = len(arr)

for i in range(1, N):
    for j in reversed(range(1, i + 1)):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
