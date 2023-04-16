num, m = map(int, input().split())
num_list = []
stack = []
cnt = 0

for i in str(num):
    num_list.append(int(i))

for x in num_list:
    while stack and cnt != m and stack[-1] < x:
        stack.pop()
        cnt += 1
    stack.append(x)

stack = stack[:m + 1]

for x in stack:
    print(x, end="")
