import sys

N = sys.stdin.readline().rstrip()
arr = [0 for _ in range(10)]

for x in N:
    x = int(x)
    if x == 6 or x == 9:
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[x] += 1

print(max(arr))
