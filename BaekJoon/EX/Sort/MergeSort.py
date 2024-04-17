# Merge Sort
# Divide and Conquer + Recursive
# 쪼개기(N) + 합치기(NlogN)
# O(NlogN)


# 이미 정렬되어 있는 arr[start:mid]와 arr[mid:end]를 arr[start:end]로 합침
def merge(start, end):
    tmp = []  # 작은 배열 2개를 합칠 임시 배열
    mid = (start + end) // 2
    left_idx = start  # 합쳐서 정렬할 작은 배열의 첫번째 index
    right_idx = mid  # 합쳐서 정렬할 작은 배열의 첫번째 index

    # 작은 배열 2개의 첫번째 원소부터 비교하여 tmp에 쭉쭉 넣기
    for _ in range(end - start):
        if right_idx == end:
            tmp.append(arr[left_idx])
            left_idx += 1
        elif left_idx == mid:
            tmp.append(arr[right_idx])
            right_idx += 1
        elif arr[left_idx] <= arr[right_idx]:  # stable한 성질 보장!
            tmp.append(arr[left_idx])
            left_idx += 1
        else:
            tmp.append(arr[right_idx])
            right_idx += 1

    # 임시 배열 tmp에 저장한 값을 원 배열 arr로 옮김
    for i in range(start, end):
        arr[i] = tmp[i - start]


# recursive하게 분할하고 정렬
def merge_sort(start, end):
    # base condition: 배열의 크기가 1일 때 -> 아무것도 안해도 정렬이 된 것과 동일
    if start + 1 == end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)  # arr[start:mid]를 정렬
    merge_sort(mid, end)  # arr[mid:end]를 정렬
    merge(start, end)  # arr[start:mid]와 arr[mid:end]를 arr[start:end]로 합침


arr = [3, 2, 7, 116, 62, 235, 1, 23]
N = len(arr)
merge_sort(0, N)
print(*arr)
