from collections import deque

N, K = map(int, input().split())

queue = deque([x for x in range(1, N + 1)])

acc = 1
while len(queue) != 1:
    if acc % K == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    acc += 1

print(queue.popleft())
