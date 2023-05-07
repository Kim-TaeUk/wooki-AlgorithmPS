input1 = input()
input2 = input()
str1 = [0] * 52
str2 = [0] * 52

for x in input1:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1
for x in input2:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

# ASCII
# A ~ Z : 65 ~ 90 -> 0 ~ 25
# a ~ z : 97 ~ 122 -> 26 ~ 51
