import sys

N, K = map(int, sys.stdin.readline().split())

josephus = list(range(1, N + 1))
res = []
idx = 0

while josephus:
    idx += K - 1
    if idx >= len(josephus):
        idx %= len(josephus)
    res.append(josephus.pop(idx))

print("<", end="")
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end=">")
    else:
        print(res[i], end=", ")

# dequq 굳이 쓰지 않고, 요소를 건너뛰면서 pop하는 풀이
# 시간복잡도 O(N), 이전 풀이는 O(NK)
