# Selection Sort
# O(N^2)

# Min-Selection Sort
arr1 = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
N = len(arr1)

for i in range(N - 1):
    min_index = i
    for j in range(i + 1, N):  # 이미 정렬된 값은 비교 X
        if arr1[min_index] > arr1[j]:
            min_index = j
    arr1[i], arr1[min_index] = arr1[min_index], arr1[i]

# Max-Selection Sort
arr2 = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
N = len(arr2)

for i in reversed(range(1, N)):
    max_index = i
    for j in range(0, i):
        if arr2[max_index] < arr2[j]:
            max_index = j
    arr2[i], arr2[max_index] = arr2[max_index], arr2[i]
