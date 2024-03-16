import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0
num = N
while True:
    A = N // 10
    B = N % 10
    N = 10 * B + (A + B) % 10
    cnt += 1
    if N == num:
        break
print(cnt)
