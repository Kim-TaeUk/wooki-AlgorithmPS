import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    function = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    numbers = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    flag = 1  # 1이면 그대로, -1이면 뒤집은 상태

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
                flag *= -1
            elif command == "D":
                if numbers:
                    if flag == 1:
                        numbers.popleft()
                    elif flag == -1:
                        numbers.pop()
                else:
                    print('error')
                    break
    else:
        if numbers:
            numbers = [int(number) for number in numbers]
            print("[", end="")
            if flag == 1:
                for i in range(len(numbers)):
                    if i != len(numbers) - 1:
                        print(numbers[i], end=",")
                    else:
                        print(numbers[i], end="]")
                        print()
            elif flag == -1:
                for i in range(len(numbers) - 1, -1, -1):
                    if i != 0:
                        print(numbers[i], end=",")
                    else:
                        print(numbers[i], end="]")
                        print()
        else:
            print('[]')

# numbers.reverse()는 시간복잡도가 O(N)
# N짜리 배열을 reverse()하면 시간복잡도 O(N^2) -> 시간 초과
# reverse()하지 않고, flag 도입해서 해결
