K, N = map(int, input().split())
k_list = []
for _ in range(K):
    k_list.append(int(input()))

res = 0
left = 1
right = max(k_list)

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for x in k_list:
        cnt += x // mid
    if cnt >= N:
        res = mid
        left = mid + 1
    else:  # cnt>N
        right = mid - 1

print(res)
