L = int(input())
L_list = list(map(int, input().split()))
M = int(input())

L_arr = [0] * 101
max = float('-inf')
min = float('inf')

for x in L_list:
    L_arr[x] += 1
    if x > max:
        max = x
    if x < min:
        min = x

for _ in range(M):
    if L_arr[max] == 1:
        L_arr[max] -= 1
        max -= 1
        L_arr[max] += 1
    else:
        L_arr[max] -= 1
        L_arr[max - 1] += 1

    if L_arr[min] == 1:
        L_arr[min] -= 1
        min += 1
        L_arr[min] += 1
    else:
        L_arr[min] -= 1
        L_arr[min + 1] += 1

print(max - min)
