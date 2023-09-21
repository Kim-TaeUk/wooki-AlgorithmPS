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
        myset = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20'}
    elif order[0] == 'empty':
        myset.clear()

# 시간 초과 - 'all' 조건에서 집합 직접 할당으로 해결
# 비트 마스킹으로도 해결 가능하다고 함..
