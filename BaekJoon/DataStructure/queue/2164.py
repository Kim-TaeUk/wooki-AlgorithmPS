import sys

N = int(sys.stdin.readline().rstrip())
numbers = [x + 1 for x in range(N)]

while numbers:
    numbers.pop(0)
    if len(numbers) == 1:
        print(numbers[0])
        break
    else:
        numbers.append(numbers.pop(0))

# 문제 그대로 구현 - 시간 초과
