import sys

A = int(sys.stdin.readline().rstrip())
op = sys.stdin.readline().rstrip()
B = int(sys.stdin.readline().rstrip())

if op == "*":
    print(A * B)
else:
    print(A + B)
