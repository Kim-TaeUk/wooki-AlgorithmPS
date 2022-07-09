# 7. 문자열과 내장 함수
msg = "It is Time"

# upper & lower
print(msg.upper())
print(msg.lower())
print(msg)  # 문자열 원본은 그대로

# find & count
tmp = msg.upper()  # 원본 바뀜
print(tmp.find('T'))  # 1
print(tmp.count('T'))  # 2

# slice
print(msg[:2])  # index ~ 1
print(msg[4:])  # index 5 ~
print(msg[3:5])  # index 3 ~ 4

print(len(msg))  # 10

# 문자열 접근
for i in range(len(msg)):  # 이거랑 아래랑
    print(msg[i], end=' ')
print()

for i in msg:  # 똑같다
    print(i, end=' ')
print()

# isupper & islower & isalpha
for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():  # 알파벳만 출력 = 공백 없이 출력
        print(x, end='')
print()

# ord(ASCII) & chr
tmp = 'AZ'
for x in tmp:
    print(ord(x))  # A65 Z90
print()

tmp = 65
print(chr(tmp))
