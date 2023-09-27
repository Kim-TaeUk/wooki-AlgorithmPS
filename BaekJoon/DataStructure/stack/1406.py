import sys

left_stack = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
right_stack = []

for _ in range(M):
    command = sys.stdin.readline().split()

    if command[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif command[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif command[0] == 'B' and left_stack:
        left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

res = left_stack + right_stack[::-1]

for item in res:
    print(item, end="")

# stack 2개 사용하여 해결
