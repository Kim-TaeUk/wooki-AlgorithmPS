import sys

S = sys.stdin.readline().rstrip()
count = [0 for _ in range(26)]

for x in S:
    count[ord(x) - 97] += 1

print(*count)
