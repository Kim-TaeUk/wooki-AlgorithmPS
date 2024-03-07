import sys

MOD = 1000000007


def merge(left_value, right_value):
    return (left_value * right_value) % MOD


def build(node, arr_start_index, arr_end_index):
    if arr_start_index == arr_end_index:
        segment_tree[node] = arr[arr_start_index]
        return segment_tree[node]

    mid_index = arr_start_index + (arr_end_index - arr_start_index) // 2
    left_value = build(node * 2, arr_start_index, mid_index)
    right_value = build(node * 2 + 1, mid_index + 1, arr_end_index)
    segment_tree[node] = merge(left_value, right_value)

    return segment_tree[node]


def query(left, right, node, arr_start_index, arr_end_index):
    if right < arr_start_index or left > arr_end_index:
        return 1

    if left <= arr_start_index and right >= arr_end_index:
        return segment_tree[node]

    mid = arr_start_index + (arr_end_index - arr_start_index) // 2
    return merge(query(left, right, node * 2, arr_start_index, mid)
                 , query(left, right, node * 2 + 1, mid + 1, arr_end_index))


def update(arr_index, new_value, node, arr_start_index, arr_end_index):
    if arr_index < arr_start_index or arr_index > arr_end_index:
        return segment_tree[node]

    if arr_start_index == arr_end_index:
        segment_tree[node] = new_value
        return segment_tree[node]

    mid = arr_start_index + (arr_end_index - arr_start_index) // 2
    left_value = update(arr_index, new_value, node * 2, arr_start_index, mid)
    right_value = update(arr_index, new_value, node * 2 + 1, mid + 1, arr_end_index)
    segment_tree[node] = merge(left_value, right_value)

    return segment_tree[node]


N, M, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
segment_tree = [0] * (N * 4)
build(1, 0, N - 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(b - 1, c, 1, 0, N - 1)
    if a == 2:
        print(query(b - 1, c - 1, 1, 0, N - 1))
