bar = input()
stack = []
res = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    else:  # )일 때
        stack.pop()
        if bar[i - 1] == '(':  # ()일 때 -> 레이저로자르니까
            res += len(stack)  # 레이저로 잘린 개수 더해주기(stack 길이)
        else:  # )로 닫는거, 오른쪽 끝에 잘린 조각만 남음
            res += 1  # 자투리 조각만 +1

print(res)

# 굳이 list(input())으로 받지 않아도 됨
# stack.pop()은 공통된 부분이니까 한 번에 처리하기
