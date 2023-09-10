N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()

cnt = 0

while N_list:
    if len(N_list) == 1:
        cnt += 1
        break

    if N_list[0] + N_list[-1] > M:
        N_list.pop()
        cnt += 1
    else:
        N_list.pop(0)
        N_list.pop()
        cnt += 1

print(cnt)

# deque 안쓰는 풀이
# pop(0)
