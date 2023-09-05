N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for x in M_list:
    if x not in N_list:
        print(0, end=" ")
    else:
        print(1, end=" ")
