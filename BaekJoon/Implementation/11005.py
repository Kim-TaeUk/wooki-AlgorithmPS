import sys

N, B = map(int, sys.stdin.readline().split())
res = ''
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while N:
    res += str(arr[N % B])
    N //= B
print(res[::-1])
