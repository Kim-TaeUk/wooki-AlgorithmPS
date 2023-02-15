def solution(n):
    myList = list(str(n))
    myList.sort(reverse=True)
    return int("".join(myList))
