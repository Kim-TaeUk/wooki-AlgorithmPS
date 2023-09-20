T = int(input())

for _ in range(T):
    PS = input()
    stack = []

    for x in PS:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
