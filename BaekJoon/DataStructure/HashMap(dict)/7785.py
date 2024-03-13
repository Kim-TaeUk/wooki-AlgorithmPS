import sys

n = int(sys.stdin.readline().rstrip())
log = dict()
for _ in range(n):
    name, status = map(str, sys.stdin.readline().split())
    if status == 'enter':
        log[name] = 1
    if status == 'leave':
        del log[name]

for name in sorted(log.keys(), reverse=True):
    print(name)
