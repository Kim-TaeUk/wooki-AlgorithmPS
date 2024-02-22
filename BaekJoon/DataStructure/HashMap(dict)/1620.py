import sys

N, M = map(int, sys.stdin.readline().split())
book = dict()
koob = dict()

for i in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    book[i] = name
    koob[name] = i

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(book[int(question)])
    else:
        print(koob[question])
