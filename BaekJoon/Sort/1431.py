import sys


def serial_sum(serial):
    res = 0
    for x in serial:
        if x.isdigit():
            res += int(x)
    return res


N = int(sys.stdin.readline().rstrip())
numbers = [sys.stdin.readline().rstrip() for _ in range(N)]
numbers.sort(key=lambda x: (len(x), serial_sum(x), x))

for number in numbers:
    print(number)
