N = int(input())
list = list(map(int, input().split()))

avg = round(sum(list) / N)

min = float('inf')
for idx, x in enumerate(list):  # enumerate 이용
    deviation = abs(x - avg)  # 편차 계산
    if deviation < min:  # 편차가 min 보다 더 작다면
        min = deviation  # 편차로 min을 재정의
        score = x  # score는 점수로
        res = idx + 1  # res는 인덱스 + 1로
    elif deviation == min:  # 편차가 min과 같고 -> 편차가 같은 다른 점수를 만났을 때
        if x > score:  # 이 점수가 score보다 크다면 -> 크거나 같다고 처리하지 않았으므로 학생번호가 빠른 번호가 답이 됨
            score = x  # score를 이 점수로 갱신하고
            res = idx + 1  # res는 인덱스 + 1로

print(avg, res)

# 내 풀이에서는 enumerate를 사용하지 않아서 코드가 길어졌음 -> 사용을 하자!!
# case 분류를 바보같이 함 -> 한 번에 처리할 수 있는 것을 2번에 처리하니까 코드가 길어지고 반복문을 많이 사용함
