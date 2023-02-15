def solution(x):
    myList = list(str(x))
    sum = 0
    for k in myList:
        sum += int(k)

    if x % sum == 0:
        return True
    else:
        return False
