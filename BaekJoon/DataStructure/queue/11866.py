import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

josephus = deque(list(range(1, N + 1)))
res = []

while josephus:
    for _ in range(K - 1):
        josephus.append(josephus.popleft())

    res.append(josephus.popleft())

print("<", end="")
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end=">")
    else:
        print(res[i], end=", ")
