def iterative_mergesort(list):  # iterative merge sort
    width = 1  # 처음 width를 2의 0승인 1로

    while width < len(list):
        l = 0  # 항상 왼쪽 끝에서부터 시작해야 하므로 0으로

        while l < len(list):
            # list의 마지막 원소까지 확인해야하니까 len(list)-1까지만 돌게 한다
            xxx = l + width * 2 - 1
            yyy = l + width - 1
            r = min(l + (width * 2 - 1), len(list) - 1)
            m = min(l + width - 1, len(list) - 1)
            # r과 m은 min으로 묶었기 때문에 len(list)-1 = 9가 되기 전까지 계속 앞의 parameter가
            # 선택되기 때문에 모든 case를 핸들링할 수 있다

            merge(list, l, m, r)
            l += width * 2
        width *= 2
        # l=10, 즉 list의 끝까지 탐색했을 경우 2배를 늘려
        # 1칸->2칸->4칸 이런 식으로 정렬 범위를 늘린다
        # width가 2배씩 증가해서 length보다 커지게 되면 다 정렬이 됐다는 의미가 된다
        print(list)
    return list


def merge(list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    # mid가 재설정됨에 따라 배열의 개수가 달라짐

    L = [0] * n1
    R = [0] * n2
    # mid의 크기에 의존적인 배열 선언

    for i in range(0, n1):  # L에 원소 채워 넣기
        L[i] = list[left + i]
    for i in range(0, n2):  # R에 원소 채워 넣기
        R[i] = list[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] <= R[j]:  # sublist에 저장한 값들끼리 비교하여
            list[k] = L[i]  # L의 원소를 정렬할 list에 넣고
            i += 1  # i를 하나 증가시키거나
        else:
            list[k] = R[j]  # R의 원소를 정렬할 list에 넣고
            j += 1  # j를 하나 증가 시킨다
        k += 1  # 1회 시행마다 k를 하나 증가킨다

    # while문 2개로 i와 n1, j와 n2의 크기 비교해서 정렬시킨다
    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1


A = [30, 20, 40, 35, 5, 50, 45, 10, 25, 15]
print("정렬 전의 배열 : ", A)
print("정렬 후의 배열 : ", iterative_mergesort(A))
