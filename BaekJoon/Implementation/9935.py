import sys


def factory():
    tmp = []
    tmp.append(words)
    while True:
        before = tmp.pop()
        after = before.replace(bomb, "")
        tmp.append(after)
        if before == after:
            if after == '':
                return 'FRULA'
            return after


words = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
print(factory())
