import sys


def convert(time):
    return int(time.replace(':', ''))


S, E, Q = map(convert, sys.stdin.readline().split())
book = set()
cnt = 0
while True:
    try:
        time, name = sys.stdin.readline().split()
        time = convert(time)
        if time <= S:
            book.add(name)
        elif E <= time <= Q:
            if name in book:
                book.remove(name)
                cnt += 1
    except:
        break

print(cnt)
