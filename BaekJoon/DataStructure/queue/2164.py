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

# N=1일 때, 런타임 에러 -> 예외 처리
# pop(0) - 시간복잡도 O(N)
# popleft() - 시간복잡도 O(1)


# list VS deque
# deque: double linked list로 구현되어 있음

# random access의 경우 list는 O(1), deque는 순차적으로 이동해야해서 O(N)
# list에서 pop()은 O(1), pop(0)은 O(N) -> 한 칸씩 앞으로 이동시켜야 해서
# deque에서 popleft(), appendleft()는 O(1)
