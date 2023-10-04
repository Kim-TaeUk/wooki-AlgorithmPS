import sys

words = []
length = []

for _ in range(5):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    length.append(len(word))

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            print(words[j][i], end="")
