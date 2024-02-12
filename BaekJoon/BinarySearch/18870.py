import sys

N = int(sys.stdin.readline().rstrip())
X_list = list(map(int, sys.stdin.readline().split()))

sortedX_list = sorted(set(X_list))

for x in X_list:
    left = 0
    right = len(sortedX_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sortedX_list[mid] == x:
            print(mid, end=' ')
            break
        elif sortedX_list[mid] < x:
            left = mid + 1
        elif sortedX_list[mid] > x:
            right = mid - 1

# sortedX_list.index(x)을 써볼까 했는데,
# python 내부에서 순차 탐색으로 구현되어 있기 때문에 시간복잡도가 N^2여서 시간 초과
