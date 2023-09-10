from collections import deque

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()
dq = deque(N_list)

cnt = 0

while dq:
    if len(dq) == 1:
        cnt += 1
        break

    if dq[0] + dq[-1] > M:
        dq.pop()
        cnt += 1
    else:
        dq.pop()
        dq.popleft()
        cnt += 1

print(cnt)
