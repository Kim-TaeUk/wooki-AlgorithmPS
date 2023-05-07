input1 = input()
input2 = input()
str1 = dict()
str2 = dict()

for x in input1:
    str1[x] = str1.get(x, 0) + 1

for x in input2:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():  # str1의 key를 하나씩 도는데,
    if i in str2.keys():  # str2에는 있는 key인데
        if str1[i] != str2[i]:  # 2)value값이 다르면 바로 NO
            print("NO")
            break
    else:  # 1)str2에는 없는 key라면 바로 NO
        print("NO")
        break
else:  # str2에 있는 키이고, value값도 모든 i에 대해서 같다면 YES
    print("YES")

# Anagram 해결하는 방법은 2가지 방법이 있다.
# 1. sort한 다음 비교 / 2. hash로 카운트하여 비교
# sorted의 시간 복잡도는 O(N log N)
# hash의 시간 복잡도는 O(N)

# 딕셔너리 get 함수 사용하기 -> default 0 넣어주는 아이디어
