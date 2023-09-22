import sys

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

cards = {}

for x in N_list:
    if x in cards:
        cards[x] += 1
    else:
        cards[x] = 1

for x in M_list:
    if x in cards:
        print(cards[x], end=" ")
    else:
        print(0, end=" ")
