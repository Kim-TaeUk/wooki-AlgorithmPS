N = int(input())
N_list = list(map(int, input().split()))

left = 0
right = N - 1
last = 0
res = ""
tmp = []

while left <= right:
    if N_list[left] > last:
        tmp.append((N_list[left], 'L'))
    if N_list[right] > last:
        tmp.append((N_list[right], 'R'))

    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]

        if tmp[0][1] == 'L':
            left += 1
        else:
            right -= 1

    tmp.clear()

print(len(res))
print(res)
