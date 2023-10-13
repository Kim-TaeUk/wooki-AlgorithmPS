import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().rstrip())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60

if A >= 24:
    A -= 24

print(A, B)
