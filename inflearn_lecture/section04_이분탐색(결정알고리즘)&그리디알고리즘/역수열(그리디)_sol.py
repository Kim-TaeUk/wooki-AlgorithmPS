N = int(input())
reverse_list = list(map(int, input().split()))

original_list = [0] * N

for i in range(N):
    for j in range(N):
        if reverse_list[i] == 0 and original_list[j] == 0:
            original_list[j] = i + 1
            break
        elif original_list[j] == 0:
            reverse_list[i] -= 1

for x in original_list:
    print(x, end=" ")
