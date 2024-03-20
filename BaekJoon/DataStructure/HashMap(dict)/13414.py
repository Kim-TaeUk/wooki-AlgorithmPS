import sys

K, L = map(int, sys.stdin.readline().split())
waiting = dict()
for i in range(L):
    number = sys.stdin.readline().rstrip()
    waiting[number] = i

sorted_lst = sorted(waiting.items(), key=lambda x: x[1])
if len(sorted_lst) < K:
    K = len(sorted_lst)

for i in range(K):
    print(sorted_lst[i][0])
