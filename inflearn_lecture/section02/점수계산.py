N = int(input())
list = list(map(int, input().split()))

score_list = []  # 점수 저장할 score_list
score = 0  # 문제에서 획득한 점수
for i in range(len(list)):
    if list[i] == 0:  # 틀렸으면
        score = 0  # 획득한 점수 0을
        score_list.append(score)  # score_list에 넣고
    elif list[i] == 1:  # 맞았으면
        score += 1  # +1해서
        score_list.append(score)  # score_list에 넣는다
        # 이때 연속해서 맞으면 elif로 계속 들어오니까 +1씩 누적됨

print(sum(score_list))
