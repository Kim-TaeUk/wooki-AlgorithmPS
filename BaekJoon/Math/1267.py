import sys

N = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().split()))

YS = 0
MS = 0
for time in times:
    YS += (time // 30 + 1) * 10
    MS += (time // 60 + 1) * 15

if YS == MS:
    print('Y M', YS)
elif YS > MS:
    print('M', MS)
else:
    print('Y', YS)
