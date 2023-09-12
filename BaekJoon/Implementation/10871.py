N, X = map(int, input().split())
N_list = list(map(int, input().split()))

for x in N_list:
    if x < X:
        print(x, end=" ")
