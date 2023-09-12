word = input()

# 내 풀이 - ASCII 이용
alphabet = [-1] * 26

for i in range(len(word)):
    if alphabet[ord(word[i]) - 97] == -1:
        alphabet[ord(word[i]) - 97] = i

for x in alphabet:
    print(x, end=" ")

# 풀이 1 - index() 이용
alphabet = "abcdefghijklmnopqrstuvwxyz"

for x in alphabet:
    if x in word:
        print(word.index(x), end=" ")
    else:
        print(-1, end=" ")

# 풀이 2 - ASCII + find() 이용
alphabet = list(range(97, 123))

for x in alphabet:
    print(word.find(chr(x)), end=" ")
