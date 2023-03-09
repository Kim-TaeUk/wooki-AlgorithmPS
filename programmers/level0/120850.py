def solution(my_string):
    answer = []
    for x in my_string:
        if not x.isalpha():
            answer.append(int(x))

    answer.sort()
    return answer
