import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline().rstrip())

print(lst.count(v))
