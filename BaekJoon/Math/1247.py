import sys

for _ in range(3):
    res = 0
    for i in range(int(sys.stdin.readline().rstrip())):
        res += int(sys.stdin.readline().rstrip())

    if not res:
        print(0)
    elif res < 0:
        print("-")
    else:
        print("+")
