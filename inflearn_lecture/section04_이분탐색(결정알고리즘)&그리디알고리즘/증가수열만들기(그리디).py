from collections import deque

N = int(input())
N_list = list(map(int, input().split()))

dq = deque(N_list)
current = 0
res = ""

left = dq.popleft()
right = dq.pop()

while len(dq) >= 0:
    if current > left and current > right:
        break
    if len(dq) == 0:
        if current < left and current < right:
            if left < right:
                res = res + 'L'
                current = left
                break
            elif left > right:
                res = res + 'R'
                current = right
                break
        elif left > current > right:
            res = res + 'L'
            current = left
            break
        elif right > current > left:
            res = res + 'R'
            current = right
            break
    else:
        if current < left and current < right:
            if left < right:
                res = res + 'L'
                current = left
                left = dq.popleft()
            elif left > right:
                res = res + 'R'
                current = right
                right = dq.pop()
        elif left > current > right:
            res = res + 'L'
            current = left
            left = dq.popleft()
        elif right > current > left:
            res = res + 'R'
            current = right
            right = dq.pop()

print(len(res))
print(res)
