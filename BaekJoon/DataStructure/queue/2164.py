import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
numbers = deque([x + 1 for x in range(N)])

while numbers:
    numbers.popleft()
    if len(numbers) == 1:
        print(numbers[0])
        break
    else:
        numbers.append(numbers.popleft())

# N=1일 때, 런타임 에러 발생..
