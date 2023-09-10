L = int(input())
L_list = list(map(int, input().split()))
M = int(input())

L_list.sort()

for _ in range(M):
    L_list[0] += 1
    L_list[L - 1] -= 1
    L_list.sort()

print(L_list[L - 1] - L_list[0])

# for문 안에 sort()가 있기 때문에 시간 초과에 취약함
