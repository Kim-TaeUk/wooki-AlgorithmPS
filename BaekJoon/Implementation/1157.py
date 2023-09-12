word = input().upper()
word_list = list(set(word))

cnt = []

for x in word_list:
    cnt.append(word.count(x))

if cnt.count(max(cnt)) != 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])
