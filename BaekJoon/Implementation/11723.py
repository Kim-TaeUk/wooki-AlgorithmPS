import sys

N = int(sys.stdin.readline().rstrip())
myset = set()

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'add':
        myset.add(order[1])
    elif order[0] == 'remove':
        myset.discard(order[1])
    elif order[0] == 'check':
        if order[1] in myset:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if order[1] in myset:
            myset.discard(order[1])
        else:
            myset.add(order[1])
    elif order[0] == 'all':
        myset = set([str(x + 1) for x in range(20)])
    elif order[0] == 'empty':
        myset.clear()

# 시간 초과
