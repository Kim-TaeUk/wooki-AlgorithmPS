import sys

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if sum(lst) == 0:
        break

    lst.sort()
    if lst[2] >= lst[0] + lst[1]:
        print("Invalid")
    elif lst[0] == lst[1] == lst[2]:
        print("Equilateral")
    elif lst[0] == lst[1] or lst[1] == lst[2] or lst[2] == lst[0]:
        print("Isosceles")
    else:
        print("Scalene")
