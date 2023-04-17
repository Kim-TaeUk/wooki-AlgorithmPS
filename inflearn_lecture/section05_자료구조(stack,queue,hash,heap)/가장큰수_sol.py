num, m = map(int, input().split())

num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:  # stack이 비어있지 않을 때만 돌아야 하는 것을 stack으로
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:  # 뒤에서 pop해야할 것이 m개 남았으니까 그냥 slicing 처리 해버리는 아이디어
    stack = stack[:-m]

res = "".join(map(str, stack))
print(res)
print(type(res))
