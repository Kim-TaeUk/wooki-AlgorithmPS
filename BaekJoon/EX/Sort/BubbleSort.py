# Bubble Sort
# O(N^2)

arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
N = len(arr)

for i in range(N):
    for j in range(N - i - 1):  # 이미 정렬된 값은 비교 X
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
