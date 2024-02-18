import sys

N, M = map(int, sys.stdin.readline().split())
dict = dict()
for _ in range(N):
    address, password = map(str, sys.stdin.readline().split())
    dict[address] = password

for _ in range(M):
    address = sys.stdin.readline().rstrip()
    print(dict.get(address))
