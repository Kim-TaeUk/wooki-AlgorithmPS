import sys

N = int(input())
words = []

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words.append((word, len(word)))

words = list(set(words))

words.sort(key=lambda x: (x[1], x[0]))

for word, length in words:
    print(word)
