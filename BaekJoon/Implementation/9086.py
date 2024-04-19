import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    strt = sys.stdin.readline().rstrip()
    print(strt[0] + strt[-1])
