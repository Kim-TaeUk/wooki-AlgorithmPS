N, M = map(int, input().split())
N_list = list(map(int, input().split()))
M_list = [list(map(int, input().split())) for _ in range(M)]

N_list.sort()

for i in range(M):
    left1 = 0
    right1 = N - 1
    left2 = 0
    right2 = N - 1
    x1 = -1
    x2 = -1

    while left1 <= right1:
        mid1 = (left1 + right1) // 2

        if M_list[i][0] < N_list[mid1]:
            right1 = mid1 - 1
        elif M_list[i][0] == N_list[mid1]:
            x1 = mid1
            break
        elif M_list[i][0] > N_list[mid1]:
            left1 = mid1 + 1

    while left2 <= right2:
        mid2 = (left2 + right2) // 2

        if M_list[i][1] < N_list[mid2]:
            right2 = mid2 - 1
        elif M_list[i][1] == N_list[mid2]:
            x2 = mid2
            break
        elif M_list[i][1] > N_list[mid2]:
            left2 = mid2 + 1

    if x1 == -1:
        x1 = left1

    if x2 == -1:
        x2 = right2
    print(x2 - x1 + 1)

# 이분 탐색 -> 시간 초과
