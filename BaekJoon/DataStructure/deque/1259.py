from collections import deque

while True:
    number = input()

    if number == '0':
        break

    number = deque(number)

    isPalindrome = True

    while number:
        if len(number) == 1:
            break
        else:
            if number.popleft() != number.pop():
                isPalindrome = False
                break

    if isPalindrome:
        print('yes')
    else:
        print('no')

# deque 사용
