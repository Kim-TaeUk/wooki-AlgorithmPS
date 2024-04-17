import sys


# Segment Tree의 왼쪽과 오른쪽 노드 이용하는 메서드
def merge(left_value, right_value):
    return left_value + right_value  # Segment Tree의 조건에 따라 +, min, max가 가능


def build(node, arr_start_index, arr_end_index):
    """
    recursive하게 Segment Tree를 만드는 메서드
    arr_start_index, arr_end_index: 원 배열의 시작 인덱스와 마지막 인덱스
    node: Segment Tree의 index
    build(1, 0, N - 1): Segment Tree의 1(node)번 인덱스는 원 배열의 0(arr_start_index) ~ N - 1(arr_end_index)를 커버하는 것!
    """
    if arr_start_index == arr_end_index:  # tree의 leaf node일 때 -> 값을 저장
        segment_tree[node] = arr[arr_start_index]
        return segment_tree[node]
        # ex) node = 16, arr_start_index = arr_end_index = 0 -> segment_tree[16] = arr[0]

    mid_index = arr_start_index + (arr_end_index - arr_start_index) // 2
    left_value = build(node * 2, arr_start_index, mid_index)  # 왼쪽 자식으로 재귀
    right_value = build(node * 2 + 1, mid_index + 1, arr_end_index)  # 오른쪽 자식을 재귀
    segment_tree[node] = merge(left_value, right_value)

    return segment_tree[node]


def query(left, right, node, arr_start_index, arr_end_index):
    """
    Segment Tree 이용하여 구간의 합을 recursive하게 구하는 메서드
    left, right:
    node: Segment Tree의 index
    arr_start_index, arr_end_index: 해당 node가 cover하는 arr(원 배열)의 범위
    -> arr[arr_start_index] ~ arr[arr_end_index]
    """
    if right < arr_start_index or left > arr_end_index:
        return 0  # default value -> sum이기 때문에 0, GCD/max/min에서는 다른 기본값 사용!

    if left <= arr_start_index and right >= arr_end_index:
        return segment_tree[node]

    mid = arr_start_index + (arr_end_index - arr_start_index) // 2
    return merge(query(left, right, node * 2, arr_start_index, mid)
                 , query(left, right, node * 2 + 1, mid + 1, arr_end_index))


def update(arr_index, new_value, node, arr_start_index, arr_end_index):
    """
    Segment Tree에서 값을 변경하는 메서드
    arr_index: update할 위치(원 배열의 index)
    new_value: update할 값
    node: Segment Tree의 index
    arr_start_index, arr_end_index: 해당 node가 cover하는 arr(원 배열)의 범위
    -> arr[arr_start_index] ~ arr[arr_end_index]
    """
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


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * (N * 4)  # Segment Tree의 공간 미리 할당

build(1, 0, N - 1)
# print(segment_tree)
# print(query(3, 10, 1, 0, N - 1))
# print(segment_tree)
# update(5, 13, 1, 0, N - 1)
# print(segment_tree)
# print(query(3, 10, 1, 0, N - 1))


"""
15
1 3 11 6 7 10 14 9 18 16 5 4 2 8 19
"""
