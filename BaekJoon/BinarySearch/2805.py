N, M = map(int, input().split())
N_list = list(map(int, input().split()))

res = 0
# left = min(N_list)
left = 1
right = max(N_list)

while left <= right:
    cnt = 0
    mid = (left + right) // 2

    for x in N_list:
        if mid < x:
            cnt += (x - mid)

    if cnt >= M:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)

# 반례
# 4 10
# 4 5 6 7
# answer = 3, but output = 0
