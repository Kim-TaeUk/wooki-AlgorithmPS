N, M = map(int, input().split())
n_list = list(map(int, input().split()))

res = 0
left = 1
right = sum(n_list)

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    acc = 0
    for x in n_list:
        if acc + x > mid:
            cnt += 1
            acc = x
        else:
            acc += x

    if cnt <= M:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
