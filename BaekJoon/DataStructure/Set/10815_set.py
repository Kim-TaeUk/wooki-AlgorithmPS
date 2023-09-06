N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for x in M_list:
    if x in N_list:
        print(1, end=" ")
    else:
        print(0, end=" ")

# list 대신 set 사용
# 포함되어 있는 것을 확인 할 때 시간복잡도는
# list: O(N), set: O(1)
