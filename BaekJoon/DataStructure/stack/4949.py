import sys
from collections import deque

while True:
    string = list(map(str, sys.stdin.readline().rstrip()))
    if string == ['.']:
        break
    string = deque([x for x in string if not x.isspace() and not x.isalpha()])
    string.pop()
    stack = []
    flag = 1

    while string:
        tmp = string.popleft()
        if tmp == '(' or tmp == '[':
            stack.append(tmp)
        else:
            if tmp == ')':
                if stack:
                    if stack.pop() != '(':
                        flag *= -1
                        break
                else:
                    flag *= -1
                    break

            elif tmp == ']':
                if stack:
                    if stack.pop() != '[':
                        flag *= -1
                        break
                else:
                    flag *= -1
                    break

    if stack:
        print('no')
    else:
        if flag == 1:
            print('yes')
        else:
            print('no')

# 코드가 너무 더럽다..
