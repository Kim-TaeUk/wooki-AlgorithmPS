import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    function = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    numbers = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    for command in function:
        if n == 0:
            if 'D' in function:
                print('error')
                break
            else:
                print('[]')
                break
        else:
            if command == "R":
                numbers.reverse()
            elif command == "D":
                if numbers:
                    numbers.popleft()
                else:
                    print('error')
                    break
    else:
        if numbers:
            numbers = [int(number) for number in numbers]
            print("[", end="")
            for i in range(len(numbers)):
                if i != len(numbers) - 1:
                    print(numbers[i], end=",")
                else:
                    print(numbers[i], end="]")
                    print()
        else:
            print('error')
