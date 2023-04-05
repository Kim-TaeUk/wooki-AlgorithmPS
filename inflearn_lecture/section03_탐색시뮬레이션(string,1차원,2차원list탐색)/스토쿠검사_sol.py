def check(input_list):
    for i in range(9):
        check_row = [0] * 10
        check_col = [0] * 10
        for j in range(9):
            check_row[input_list[i][j]] = 1
            check_col[input_list[j][i]] = 1
        if sum(check_row) != 9 or sum(check_col) != 9:
            return False

    for i in range(3):
        for j in range(3):  # block 9개 중 1개를 정하는 2중 for문
            check_block = [0] * 10
            for k in range(3):
                for s in range(3):  # 정해진 block에서 9개의 숫자를 보는 이중 for문
                    check_block[input_list[i * 3 + k][j * 3 + s]] = 1
                if sum(check_block) != 9:
                    return False


input_list = [list(map(int, input().split())) for _ in range(9)]
if check(input_list):
    print("YES")
else:
    print("NO")

# 반복문 여러 개로 처리하는거보다 checklist 3개 만들어서 처리하고,
# 멍청하게 for문 돌려서 더하고 그러지 말고, sum으로 9맞는지 확인해버리기
# input_list[i][j]를 checklist의 인덱스로 처리하는 아이디어!
