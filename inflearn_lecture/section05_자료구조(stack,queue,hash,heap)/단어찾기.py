from collections import deque

N = int(input())
already = []
answer = []
for _ in range(N):
    already.append(input())

for _ in range(N - 1):
    answer.append(input())

already = deque(already)
answer = deque(answer)

while answer:
    current = answer.popleft()
    if current in already:
        already.remove(current)

print(already.pop())
