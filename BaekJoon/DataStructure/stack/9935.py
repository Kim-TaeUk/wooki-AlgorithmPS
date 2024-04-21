import sys

words = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
bomb_len = len(bomb)

for word in words:
    stack.append(word)
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
