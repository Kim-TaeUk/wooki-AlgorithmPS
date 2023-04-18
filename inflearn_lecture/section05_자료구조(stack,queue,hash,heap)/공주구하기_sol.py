from collections import deque

N, K = map(int, input().split())

dq = list(range(1, N + 1))  # dq: list
dq = deque(dq)  # dq: queue

while dq:
    for _ in range(K - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()  # break

# for문을 잘 짜니까 굳이 acc같은 변수를 도입할 필요가 없다
