N, K = map(int, input().split())

N_list = []
for _ in range(N):
    N_list.append(int(input()))

# N_list.sort(reverse=True)
N_list = N_list[::-1]
cnt = 0

for x in N_list:
    if K >= x:
        cnt += K // x
        K = K % x
# for i in range(N - 1, -1, -1):
#     if K >= N_list[i]:
#         cnt += K // N_list[i]
#         K = K % N_list[i]

print(cnt)
