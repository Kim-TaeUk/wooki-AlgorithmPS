def solution(num_list):
    answer = []
    even_cnt = 0
    odd_cnt = 0

    for x in num_list:
        if x % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1

    answer.append(even_cnt)
    answer.append(odd_cnt)

    return answer
