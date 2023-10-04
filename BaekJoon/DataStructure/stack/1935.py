import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
postfix = deque(list(map(str, sys.stdin.readline().rstrip())))
alphabet = []
for _ in range(N):
    alphabet.append(sys.stdin.readline().rstrip())
stack = deque()
operator = {'+', '-', '*', '/'}

while postfix:
    if postfix[0] in operator:
        tmpa = stack.pop()
        if type(tmpa) == int or type(tmpa) == float:
            a = tmpa
        else:
            a = int(alphabet[ord(tmpa) - 65])

        tmpb = stack.pop()
        if type(tmpb) == int or type(tmpb) == float:
            b = tmpb
        else:
            b = int(alphabet[ord(tmpb) - 65])

        op = postfix.popleft()
        if op == '+':
            tmp = a + b
        elif op == '-':
            tmp = b - a
        elif op == '*':
            tmp = a * b
        elif op == '/':
            tmp = b / a
        stack.append(tmp)

    else:
        stack.append(postfix.popleft())

print(f"{stack.pop():.2f}")
