lst1 = [1, 3, 5, 6, 7, 12, 14, 17, 18, 19, 26, 33, 34, 38, 55, 61]
N1 = len(lst1)


def binary_search(target):  # target의 좌표(lst에서의) 반환
    global lst1
    left = 0
    right = N1 - 1

    while left <= right:
        mid = (left + right) // 2
        if lst1[mid] == target:
            return mid
        elif lst1[mid] < target:
            left = mid + 1
        elif lst1[mid] > target:
            right = mid - 1

    return -1  # target이 lst에 없는 경우 -1 return


print(binary_search(12))  # 5

lst2 = [1, 3, 5, 5, 5, 7, 12, 14, 17, 18, 19, 26, 33, 34, 38, 55, 61]
N2 = len(lst2)

'''
if lst1[mid] == target:
    return mid
결국 이 코드를 빼야함 -> 값을 찾았다고 멈추면 안되기 때문에
그럼 저 조건을 target보다 클 때, 작을 때 중 어디에 포함 시키는지!에 따라 
lower bound, upper bound가 되는 것!
'''


def lower_bound(target):
    left = 0
    right = N2 - 1

    while left <= right:
        mid = (left + right) // 2
        if lst2[mid] < target:
            left = mid + 1
        else:  # lower bound를 찾아야 하니까 right를 이동시켜야 함
            right = mid - 1
    return left


def upper_bound(target):
    left = 0
    right = N2 - 1

    while left <= right:
        mid = (left + right) // 2
        if lst2[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(lower_bound(5))  # 2
print(upper_bound(5))  # 5

print(upper_bound(5) - lower_bound(5))  # 5의 개수: 3개
print(upper_bound(6) - lower_bound(6))  # 6의 개수: 0개
print(lst2[lower_bound(4)])  # 4를 넣었는데 5가 나옴 -> 4는 없다!
