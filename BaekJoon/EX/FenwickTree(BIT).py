import sys


def sum(pos):  # arr[0] ~ arr[pos]의 합을 구하는 메서드: Prefix Sum
    pos += 1  # BIT 인덱스로 변환

    res = 0
    while pos > 0:
        res += fenwick_tree[pos]
        pos -= (pos & -pos)

    return res


def sum_range(left, right):  # arr[left] ~ arr[right]의 합을 구하는 메서드: Range Sum
    res = sum(right)
    if left > 0:
        res -= sum(left - 1)

    return res


# Fenwick Tree를 build(생성)하거나 update(갱신)하는 메서드
def add(pos, delta):  # arr[pos]를 +delta하여 갱신: arr[pos] += delta
    pos += 1

    while pos < len(fenwick_tree):
        fenwick_tree[pos] += delta
        pos += (pos & -pos)


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

fenwick_tree = [0] * (N + 1)  # Fenwick Tree의 공간 미리 할당
for i in range(N):  # Fenwick Tree 생성
    add(i, arr[i])
