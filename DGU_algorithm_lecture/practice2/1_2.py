def recursive_bubblesort(list):  # recursive bubblesort
    for i in range(len(list) - 1):  # list길이 - 1만큼 순차 탐색

        if list[i] > list[i + 1]:  # i 번째 원소와 i + 1번째 원소를 비교하고
            list[i], list[i + 1] = list[i + 1], list[i]  # 큰 값을 뒤로 보낸다
            print(A)  # 단계별로 A가 바뀌는 것을 출력r
            recursive_bubblesort(list)  # recursive하게 구현


A = [30, 20, 40, 10, 5, 1, 30, 15]
print("정렬 전의 배열 :", A)
recursive_bubblesort(A)
print("정렬 후의 배열 :", A)
