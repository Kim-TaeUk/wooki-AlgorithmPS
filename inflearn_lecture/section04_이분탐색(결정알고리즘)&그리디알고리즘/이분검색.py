# binary search
N, M = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort()  # 전제가 정렬되어 있는 상태
left = 0
right = N - 1

while left <= right:
    mid = (left + right) // 2
    if input_list[mid] == M:
        print(mid + 1)
        break
    elif input_list[mid] > M:
        right = mid - 1
    elif input_list[mid] < M:
        left = mid + 1
