import sys

A, B = map(str, sys.stdin.readline().split())
A = int(A[::-1])
B = int(B[::-1])

if A >= B:
    print(A)
else:
    print(B)
