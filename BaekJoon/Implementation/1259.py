from collections import deque

while True:
    number = input()

    if number == "0":
        break

    if number == number[::-1]:
        print('yes')
    else:
        print('no')

# 문자열로 해결