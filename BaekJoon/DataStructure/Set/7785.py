import sys

n = int(sys.stdin.readline().rstrip())
log = set()
for _ in range(n):
    name, status = map(str, sys.stdin.readline().split())
    if status == 'enter':
        log.add(name)
    if status == 'leave':
        log.remove(name)

for name in sorted(log, reverse=True):
    print(name)
