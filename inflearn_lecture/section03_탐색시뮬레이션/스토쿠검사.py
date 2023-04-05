input_list = [list(map(int, input().split())) for _ in range(9)]

# 행 체크
for i in range(9):
    temp = []
    for j in range(9):
        temp.append(input_list[i][j])

    if len(set(temp)) != 9:
        print("NO")
        exit()

# 열 체크
for i in range(9):
    temp = []
    for j in range(9):
        temp.append((input_list[j][i]))

    if len(set(temp)) != 9:
        print("NO")
        exit()

# 블럭 단위 체크 9번
temp = []
for i in range(3):
    for j in range(3):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(3):
    for j in range(3, 6):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(3):
    for j in range(6, 9):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(3, 6):
    for j in range(3):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(3, 6):
    for j in range(3, 6):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(3, 6):
    for j in range(6, 9):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(6, 9):
    for j in range(3):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(6, 9):
    for j in range(3, 6):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

temp = []
for i in range(6, 9):
    for j in range(6, 9):
        temp.append((input_list[i][j]))

if len(set(temp)) != 9:
    print("NO")
    exit()

print("YES")
