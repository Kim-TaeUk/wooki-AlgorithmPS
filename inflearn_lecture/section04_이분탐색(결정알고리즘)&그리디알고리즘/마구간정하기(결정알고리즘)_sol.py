def count(len):
    endpoint = N_list[0]  # 마지막으로 배정한 말 위치
    cnt = 1  # 말 한마리 배정

    for i in range(1, N):
        if N_list[i] - endpoint >= len:
            cnt += 1
            endpoint = N_list[i]

    return cnt


N, C = map(int, input().split())
N_list = []
for _ in range(N):
    tmp = int(input())
    N_list.append(tmp)
N_list.sort()

left = 1
right = N_list[N - 1]

while left <= right:
    mid = (left + right) // 2

    if count(mid) >= C:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
