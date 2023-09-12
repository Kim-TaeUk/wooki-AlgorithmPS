word = input()

alphabet = [-1] * 26

for i in range(len(word)):
    if alphabet[ord(word[i]) - 97] == -1:
        alphabet[ord(word[i]) - 97] = i

for x in alphabet:
    print(x, end=" ")
