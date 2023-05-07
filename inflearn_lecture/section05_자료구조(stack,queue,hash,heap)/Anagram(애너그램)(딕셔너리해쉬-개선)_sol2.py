input1 = input()
input2 = input()
strHash = dict()

for x in input1:
    strHash[x] = strHash.get(x, 0) + 1

for x in input2:
    strHash[x] = strHash.get(x, 0) - 1

for x in input1:
    if strHash.get(x) != 0:
        print("NO")
        break
else:
    print("YES")
