N = int(input())
N_list = list(map(int, input().split()))
M = int(input())

left = 0
right = max(N_list)
res = 0

while left <= right:
    mid = (left + right) // 2
    sum = 0

    for x in N_list:
        if x < mid:
            sum += x
        else:
            sum += mid

    if sum <= M:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
