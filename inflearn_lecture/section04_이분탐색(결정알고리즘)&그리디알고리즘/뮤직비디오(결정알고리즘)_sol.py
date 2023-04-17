def count(capacity):
    cnt = 1
    sum = 0
    for x in n_list:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x

    return cnt


N, M = map(int, input().split())
n_list = list(map(int, input().split()))

res = 0
left = 1
right = sum(n_list)
maxx = max(n_list)

while left <= right:
    mid = (left + right) // 2
    if mid >= maxx and count(mid) <= M:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
