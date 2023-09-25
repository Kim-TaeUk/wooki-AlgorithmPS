import sys

N, M = map(int, sys.stdin.readline().split())
nolisten = set()
nosee = set()

for _ in range(N):
    nolisten.add(sys.stdin.readline().rstrip())

for _ in range(M):
    nosee.add(sys.stdin.readline().rstrip())

res = list(nolisten & nosee)
res.sort()

print(len(res))
for name in res:
    print(name)
