N = int(input())
list_a = list(map(int, input().split()))
M = int(input())
list_b = list(map(int, input().split()))

list_c = []
p1 = p2 = 0

while p1 < N and p2 < M:  # 마지막 요소까지 list_c에 넣으면 그만 돌도록
    if list_a[p1] < list_b[p2]:  # list_a와 list_b를 비교하며 작은 요소를 list_c에 append하는 방식
        list_c.append(list_a[p1])
        p1 += 1
    else:
        list_c.append(list_b[p2])
        p2 += 1

# list_a나 list_b에서 마지막 요소에 도달하면 남은 요소들을 list_c에 다 append해버림
if p1 == N:
    list_c = list_c + list_b[p2:]

if p2 == M:
    list_c = list_c + list_a[p1:]

for x in list_c:
    print(x, end=' ')

# sort()를 쓰면 시간 복잡도 : NlogN
# 위 풀이의 시간 복잡도 : N
