N = int(input())
list_a = list(map(int, input().split()))
M = int(input())
list_b = list(map(int, input().split()))

res = list_a + list_b
res.sort()

for x in res:
    print(x, end=' ')
