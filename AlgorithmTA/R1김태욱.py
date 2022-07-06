# R - 1

n = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 오름차순 정렬해서 편하게 접근

result = 0  # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수

for i in arr:  # 오름차순 정렬됐으니까 공포도 낮은거부터 반복문
    count += 1  # 현재 그룹에 해당 모험가를 포함시키고
    if count >= i:  # 현재 그룹의 모험가 수 >= 해당 모험가의 공포도 -> 그룹 만들기
        result += 1  # 총 그룹 수 +1
        count = 0  # 다음 그룹도 세야 하니까, 그룹에 포함된 모험가 수 초기화

print(result)
