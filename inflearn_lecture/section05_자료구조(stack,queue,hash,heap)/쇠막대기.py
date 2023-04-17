bar_list = list(input())
stack = []
res = 0

for i in range(len(bar_list)):
    if bar_list[i] == '(':
        stack.append(bar_list[i])
    else:  # )일 때
        if bar_list[i - 1] == '(':  # ()일 때 -> 레이저로자르니까
            stack.pop()
            res += len(stack)  # 레이저로 잘린 개수 더해주기(stack 길이)
        else:  # )로 닫는거, 오른쪽 끝에 잘린 조각만 남음
            stack.pop()
            res += 1  # 자투리 조각만 +1

print(res)
