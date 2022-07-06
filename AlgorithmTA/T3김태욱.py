# T - 3
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    total = 0  # 총 잘리는 떡의 길이
    mid = (start + end) // 2
    for x in array:
        if x > mid:  # 떡 길이 > mid 일때만 절단 가능
            total += x - mid  # 떡길이 - 절단기 길이
    if total < m:  # 요청한 떡 길이보다 작을 때 mid를 줄여서 더 많이 자름(좌측 탐색)
        end = mid - 1
    else:  # 요청한 덕 길이보다 길 때 mid를 늘려서 더 조금 자름(우측 탐색)
        result = mid  # 최대한 덜 자를 때가 정답이니까
        start = mid + 1  # 종료점을 증가시킬 순 없고, 종료점을 감소시키면 떡 길이가 더 길어짐

print(result)
