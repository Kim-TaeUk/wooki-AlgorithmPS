import sys

N = int(sys.stdin.readline().rstrip())

numbers = set(map(int, sys.stdin.readline().split()))

numbers = list(numbers)
numbers.sort()

for number in numbers:
    print(number, end=" ")
