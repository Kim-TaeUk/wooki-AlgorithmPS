import sys

N, M = map(int, sys.stdin.readline().split())
dct = dict()
for _ in range(N):
    team = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline().rstrip())
    for _ in range(num):
        member = sys.stdin.readline().rstrip()
        dct[member] = team

for _ in range(M):
    name = sys.stdin.readline().rstrip()
    flag = int(sys.stdin.readline().rstrip())
    if flag == 0:
        print("\n".join(sorted([key for key, value in dct.items() if value == name])))
    if flag == 1:
        print(dct[name])
