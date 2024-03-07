import sys

N = int(sys.stdin.readline().rstrip())
A_list = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

ans = N
for A in A_list:
    A -= B
    if A > 0:
        if A % C == 0:
            ans += A // C
        else:
            ans += A // C + 1

print(ans)
