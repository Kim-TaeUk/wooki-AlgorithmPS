import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    sentence = sys.stdin.readline().split()
    print(" ".join(sentence[::-1])[::-1])
