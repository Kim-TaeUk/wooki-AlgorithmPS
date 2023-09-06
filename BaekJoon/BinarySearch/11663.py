N, M = map(int, input().split())
N_list = list(map(int, input().split()))
M_list = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    cnt = 0
    for x in N_list:
        if M_list[i][0] <= x <= M_list[i][1]:
            cnt += 1
    print(cnt)

# 이중 for문 -> 시간 초과
