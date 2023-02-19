def solution(s):
    mylist = list(map(int, s.split(" ")))
    return str(min(mylist)) + " " + str(max(mylist))
