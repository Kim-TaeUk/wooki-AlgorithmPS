input_string = input()
stack = []

for x in input_string:
    if x.isdigit():
        stack.append(int(x))
    else:
        tmp2 = stack.pop()
        tmp1 = stack.pop()

        if x == '+':
            stack.append(tmp1 + tmp2)
        elif x == '-':
            stack.append(tmp1 - tmp2)
        elif x == '*':
            stack.append(tmp1 * tmp2)
        elif x == '/':
            stack.append(tmp1 / tmp2)

print(stack.pop())
