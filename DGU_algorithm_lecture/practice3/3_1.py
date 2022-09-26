def recursive_mergesort(list):  # recursive mergesort -> divide하는 함수
    if len(list) < 2:  # list의 길이가 2보다 작으면 더 이상 divide할 수 없기 때문에
        return list  # list를 리턴

    mid = len(list) // 2  # mid를 list의 중간 index로 정하고
    left_list = list[:mid]  # left_list와
    right_list = list[mid:]  # right_list로 분리한다

    left_list = recursive_mergesort(left_list)  # recursive하게 left_list와
    right_list = recursive_mergesort(right_list)  # right_list에 recursive하게 구현
    print(left_list, right_list)

    # divide가 끝나면
    return merge(left_list, right_list)  # merge(left,right)를 이용하여 combine한다


def merge(left_list, right_list):
    sorted_list = []  # 정렬시켜서 출력할 배열

    while len(left_list) > 0 or len(right_list) > 0:
        # left_list와 right_list의 원소가 없을 때까지 반복하는데,
        print("정렬 중인 배열 : ", sorted_list)  # 단계별로 값의 변화를 보여주는 print문
        if len(left_list) > 0 and len(right_list) > 0:
            # left_list와 right_list에 모두 원소가 있을 때에는
            if left_list[0] <= right_list[0]:
                # left_list와 right_list의 0번째 인덱스의 값을 비교하여
                # right_list의 0번째 인덱스의 값이 크거나 같으면
                sorted_list.append(left_list[0])  # sorted_list에 넣고
                left_list = left_list[1:]  # 넣은 값을 원래 list에서 지운다
            else:
                # left_list와 right_list의 0번째 인덱스의 값을 비교하여
                # left_list의 0번째 인덱스의 값이 크거나 같으면
                sorted_list.append(right_list[0])  # sorted_list에 넣고
                right_list = right_list[1:]  # 넣은 값을 원래 list에서 지운다
        # elif절 2개는 둘 중 하나의 list에만 원소가 존재할 때인데,
        elif len(left_list) > 0:  # left_list에만 원소가 존재할 때
            sorted_list.append(left_list[0])  # sorted_list에 0번째 인덱스 값을 넣고
            left_list = left_list[1:]  # 넣은 값을 원래 list에서 지운다
        elif len(right_list) > 0:  # right_list에만 원소가 존재할 때
            sorted_list.append(right_list[0])  # sorted_list에 0번째 인덱스 값을 넣고
            right_list = right_list[1:]  # 넣은 값을 원래 list에서 지운다

    return sorted_list  # 정렬된 sorted_list를 반환한다


A = [30, 20, 40, 35, 5, 50, 45, 10, 25, 15]
print("정렬 전의 배열 : ", A)
print("정렬 후의 배열 : ", recursive_mergesort(A))
