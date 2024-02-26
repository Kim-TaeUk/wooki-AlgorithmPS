import sys


def sum(pos):
    pos += 1
    res = 0
    while pos > 0:
        res += fenwick_tree[pos]
        pos &= pos - 1
    return res


def sum_range(left, right):
    res = sum(right)
    if left > 0:
        res -= sum(left - 1)
    return res


def add(pos, delta):
    pos += 1
    while pos < len(fenwick_tree):
        fenwick_tree[pos] += delta
        pos += pos & -pos


N, M, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
fenwick_tree = [0] * (N + 1)
for i in range(N):
    add(i, arr[i])
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        add(b - 1, c - arr[b - 1])
        arr[b - 1] = c  # 원 배열에서 갱신해주기..!
    if a == 2:
        print(sum_range(b - 1, c - 1))
