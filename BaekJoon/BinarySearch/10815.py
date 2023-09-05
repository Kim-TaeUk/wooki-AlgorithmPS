N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

M_dict = dict.fromkeys(M_list)

N_list.sort()
M_list.sort()

for i in range(len(M_list)):
    left = 0
    right = len(N_list) - 1

    while True:
        mid = (left + right) // 2

        if left <= right:
            if N_list[mid] > M_list[i]:
                right = mid - 1
            elif N_list[mid] < M_list[i]:
                left = mid + 1
            elif N_list[mid] == M_list[i]:
                # print(1, end=" ")
                M_dict[M_list[i]] = 1
                N_list.remove(N_list[mid])
                break
        else:
            # print(0, end=" ")
            M_dict[M_list[i]] = 0
            break

for ans in M_dict:
    print(M_dict[ans], end=" ")

# 이분 탐색 + list 대신 dict -> 시간 초과
