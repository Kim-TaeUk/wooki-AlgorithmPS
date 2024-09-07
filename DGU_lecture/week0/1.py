class stack1:
    def __init__(self, maxindex):
        self.point = 0
        self.maxindex = maxindex
        self.stack = []

    def __del__(self):
        print("종료 시점 포인트 위치 : " + str(self.point))
        print("종료 시점 데이터 상태 : ")
        print(self.stack)

    def push(self, v):
        self.point += 1
        self.stack.append(v)

    def pop(self):
        self.point -= 1
        temp = self.stack[self.point]
        self.stack.pop()
        return temp

    def empty(self):
        if not self.stack:
            return True
        else:
            return False

    def cur_print(self):
        print("현재 시점 포인트 위치 : " + str(self.point))
        print("현재 데이터 상태 : ")
        print(self.stack)


inputs = input().split()
stack = stack1(len(inputs))

for x in inputs:
    if x.isdigit():
        stack.push(x)
        stack.cur_print()
    else:
        b = int(stack.pop())
        a = int(stack.pop())

        if x == '+':
            result = a + b
        elif x == '-':
            result = a - b
        elif x == '*':
            result = a * b
        elif x == '/':
            result = a // b

        stack.push(result)
        stack.cur_print()

print("최종 데이터 :", stack.pop())
