# summed area table (integral image)

lst = [[3, 1, 5, 7, 2],
       [9, 4, 8, 9, 7],
       [3, 9, 2, 3, 6],
       [2, 7, 5, 6, 1],
       [4, 6, 8, 5, 3],
       [3, 5, 9, 2, 7]]
N = len(lst)  # 6
M = len(lst[0])  # 5

# 누적 합 배열 만들기
summed_area = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        summed_area[i + 1][j + 1] = (lst[i][j]  # lst[i][j]에
                                     + summed_area[i][j + 1]  # 왼쪽 누적합 더하고
                                     + summed_area[i + 1][j]  # 위쪽 누적합 더해서
                                     - summed_area[i][j])  # 교집합 누적합 빼기(두번 더해진 부분)
# summed_area[i + 1][j + 1]: lst[i][j]까지의 누적합
'''
summed_area = [[0, 0, 0, 0, 0, 0],
       [0, 3, 4, 9, 16, 18],
       [0, 12, 17, 30, 46, 55],
       [0, 15, 29, 44, 63, 78],
       [0, 17, 38, 58, 83, 99],
       [0, 21, 48, 76, 106, 125],
       [0, 24, 56, 93, 125, 151]]
'''

# 구간 합 구하기
# arr[x1][x1] ~ arr[x2][y2] 구간 합
x1, y1 = 1, 2
x2, y2 = 3, 4
# [8, 9, 7]
# [2, 3, 6]
# [5, 6, 1]
region_sum = (summed_area[x2 + 1][y2 + 1]
              - summed_area[x1][y2 + 1]
              - summed_area[x2 + 1][y1]
              + summed_area[x1][y1])
print(region_sum)  # 47
