import sys

A, B = map(int, sys.stdin.readline().split())
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

res = []
count = 0
B_list.sort()

for x in A_list:
    left = 0
    right = B - 1

    while left <= right:
        mid = (left + right) // 2

        if x == B_list[mid]:
            break
        elif x > B_list[mid]:
            left = mid + 1
        elif x < B_list[mid]:
            right = mid - 1

    if left > right:
        res.append(x)
        count += 1

if count == 0:
    print(0)
else:
    print(len(res))
    res.sort()
    for x in res:
        print(x, end=" ")
