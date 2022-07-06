# T - 2

from bisect import bisect_left, bisect_right


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)  # 오른쪽 인덱스 구하고
    left_index = bisect_left(array, left_value)  # 왼쪽 인덱스 구해서
    return right_index - left_index  # 빼주면 left_value ~ right_value인 데이터 개수


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)  # 값이 [x, x] 범위에 있는 데이터 개수 계산

if count == 0:  # 값이 x인 원소가 없을 때
    print(-1)

else:  # 값이 x인 원소가 있을 때
    print(count)
