list = []
for i in range(21):
    list.append(i)

for i in range(10):
    a, b = map(int, input().split())

    temp = list[a:b + 1]
    temp.reverse()
    list[a:b + 1] = temp

for i in range(1, len(list)):
    print(list[i], end=' ')
