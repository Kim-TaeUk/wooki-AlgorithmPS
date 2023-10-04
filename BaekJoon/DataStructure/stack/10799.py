import sys

bar = list(map(str, sys.stdin.readline().rstrip()))
stack = []
res = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    else:
        stack.pop()
        if bar[i - 1] == '(':
            res += len(stack)
        else:
            res += 1

print(res)
