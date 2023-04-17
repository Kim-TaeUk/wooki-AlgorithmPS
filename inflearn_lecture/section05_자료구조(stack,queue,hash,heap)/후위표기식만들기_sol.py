input_list = input()

res = ""
stack = []

for x in input_list:
    if x.isdigit():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # stack이 빌 때까지
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()  # '('까지 pop
while stack:
    res += stack.pop()

print(res)
