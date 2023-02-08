list = []
for i in range(21):
    list.append(i)

for i in range(10):
    a, b = map(int, input().split())

    temp = list[a:b + 1]  # 구간을 temp로 따로 떼내고
    temp.reverse()  # reverse로 뒤집고
    list[a:b + 1] = temp  # 뒤집은 걸 떼어낸 데에 붙임

for i in range(1, len(list)):
    print(list[i], end=' ')
