import sys

Octal = sys.stdin.readline().rstrip()

print(bin(int(Octal, 8))[2:])

# 내장함수 이용해서 해결
