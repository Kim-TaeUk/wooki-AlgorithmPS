import sys

stack = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
cursor = len(stack)

for _ in range(M):
    command = sys.stdin.readline().split()

    if command[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor < len(stack):
            cursor += 1
    elif command[0] == 'B':
        if cursor > 0:
            stack.pop(cursor - 1)
            cursor -= 1
    elif command[0] == 'P':
        stack.insert(cursor, command[1])
        cursor += 1

for item in stack:
    print(item, end="")
