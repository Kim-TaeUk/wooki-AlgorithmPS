import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    yonsei = 0
    korea = 0
    for i in range(9):
        y, k = map(int, sys.stdin.readline().split())
        yonsei += y
        korea += k

    if yonsei < korea:
        print("Korea")
    elif yonsei > korea:
        print("Yonsei")
    else:
        print("Draw")
