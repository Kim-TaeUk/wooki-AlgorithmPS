import sys

words = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
bomb_len = len(bomb)

for word in words:
    stack.append(word)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
