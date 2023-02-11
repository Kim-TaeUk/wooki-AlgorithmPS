def solution(n):
    answer = 0

    for i in str(n):  # string으로 casting해서 하나씩 분리하고
        answer += int(i)  # 다시 int로 casting해서 더해버리기

    return answer
