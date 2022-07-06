# T - 1
def binary_search(array, left, right, target):  # 이진 탐색 함수 구현
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid  # index 반환
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
    return None  # 못찾은 경우 None 반환


n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()  # 이진 탐색 위해 정렬
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:  # 반복문 이용해서 요청한 부품 번호 확인
    x = binary_search(arr1, 0, n - 1, i)
    if x is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
