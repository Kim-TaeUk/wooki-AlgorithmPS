def solution(s):
    if len(s) == 4 or len(s) == 6:
        for x in s:
            if x.isalpha():
                return False
        else:
            return True
    else:
        return False
