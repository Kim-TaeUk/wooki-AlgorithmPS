import random  # random한 수를 뽑기 위해 random import


def recursive_quicksort(list):  # recursive quicksort
    if len(list) <= 1:  # list의 길이가 1이거나 작으면
        return list  # 바로 return한다

    pivot = list[len(list) // 2]  # 먼저 가운데에 있는 값을 pivot(기준값)으로 정한다
    left_list, right_list, equal_list = [], [], []  # pivot의 값을 기준으로 나누어 저장할 list 3개

    for x in list:  # list의 모든 원소를 탐색하는데
        if x < pivot:  # pivot보다 작으면
            left_list.append(x)  # left_list에 저장하고
        elif x > pivot:  # pivot보다 크면
            right_list.append(x)  # right_list에 저장하고
        else:  # pivot과 같으면
            equal_list.append(x)  # equal_list에 저장
        # 반복하여 진행하게 되면 pivot보다 작은 값은 모두 left_list에 몰고
        # pivot보다 큰 값은 모두 right_list에 몰 수 있다
    return recursive_quicksort(left_list) + equal_list + recursive_quicksort(right_list)
    # 좌우로 분할했던 값들을 모두 합치고 quick sort로 정렬된 list를 return


A = []
for i in range(100):  # 100개 만큼의
    k = random.randint(1, 1000)  # 난수를 1~1000에서 생성하여
    A.append(k)  # A에 append

print("정렬 전의 배열 :", A)
print("정렬 후의 배열 :", recursive_quicksort(A))
