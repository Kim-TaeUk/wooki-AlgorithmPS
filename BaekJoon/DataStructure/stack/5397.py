import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    password = sys.stdin.readline().rstrip()
    left_stack = []
    right_stack = []
    for x in password:
        if x == '-':
            if left_stack:
                left_stack.pop()
        elif x == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif x == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(x)

    res = left_stack + right_stack[::-1]
    for x in res:
        print(x, end="")
    print()
