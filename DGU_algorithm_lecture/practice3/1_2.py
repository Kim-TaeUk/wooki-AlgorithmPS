import random


def partition(list, start_index, end_index):  # partition하는 함수
    i = start_index - 1
    x = list[end_index]

    # start_index에서 end_index까지 정렬하는 반복문
    for j in range(start_index, end_index):
        if list[j] >= x:  # 내림차순이기 때문에 크거나 같을 때
            i = i + 1
            list[i], list[j] = list[j], list[i]  # 값을 swqp
    list[i + 1], list[end_index] = list[end_index], list[i + 1]
    return i + 1


def quickSortIterative(list, start_index, end_index):
    # 보조 역할을 할 stack 정의
    size = end_index - start_index + 1
    stack = [0] * size

    top = -1  # stack의 top을 초기화

    # start_index와 end_index의 초기값을 stack에 push
    top = top + 1
    stack[top] = start_index
    top = top + 1
    stack[top] = end_index

    # stack이 empty가 될 때까지 pop
    while top >= 0:

        # start_index와 end_index를 pop한다
        end_index = stack[top]
        top = top - 1
        start_index = stack[top]
        top = top - 1

        # pivot원소를 알맞은 자리에 넣음
        p = partition(list, start_index, end_index)

        # pivot 왼쪽에 있다면 왼쪽 stack에 push
        if p - 1 > start_index:
            top = top + 1
            stack[top] = start_index
            top = top + 1
            stack[top] = p - 1

        # pivot 오른쪽에 있다면 오른쪽 stack에 push
        if p + 1 < end_index:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end_index

        print(list)

    return list


A = random.sample(range(1, 100001), 10)

print("정렬 전의 배열 : ", A)
print("정렬 후의 배열 : ", quickSortIterative(A, 0, len(A) - 1))
