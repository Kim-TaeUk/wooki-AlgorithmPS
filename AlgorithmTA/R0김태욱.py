N, M = map(int, input().split())
result = 0

for i in range(N):
    data = list(map(int, input().split()))  # 반복문 이용 한 행씩 입력 받는다
    min_value = min(data)  # 현재 행에서 최솟값 찾고
    # print(min_value)
    result = max(result, min_value)  # 최솟값 중 최대값 찾기

print(result)
