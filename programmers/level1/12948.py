def solution(phone_number):
    answer = ""

    for _ in range(len(phone_number) - 4):
        answer = answer + "*"
    for i in range(len(phone_number) - 4, len(phone_number)):
        answer = answer + phone_number[i]

    return answer
