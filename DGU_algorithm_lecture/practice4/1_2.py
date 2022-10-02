# 2018112034 김태욱
# /Users/kimtaeuk/Desktop/3-2/알골/실습/4주차/example.txt
def isPanlidrome_recursive(word):
    is_palindrome = True  # 일단 is_palindrome을 True로 설정
    if len(word) <= 1:  # 한글자만 남으면 True로
        return True

    if word[0] == word[-1]:  # 첫 글자와 마지막 글자를 비교, 같으면 recursive하게 다시 함수 호출
        return isPanlidrome_recursive(word[1:-1])  # 그럼 2번째 글자와 마지막 바로 앞 글자까지로 슬라이싱 된 문자열 넘김
    else:
        is_palindrome = False

    if not is_palindrome:  # False일 때는 바로 출력
        print(word + ' is NOT palindorme')
    # recursive에서는 맨앞과 맨뒤를 slicing 계속 하기 때문에 True일 때는 다 잘려서 출력이 안됨
    # 그래서 words에 따로 저장하고 나중에 출력


with open("/Users/kimtaeuk/Desktop/3-2/알골/실습/4주차/example.txt", 'r') as file:  # 경로의 파일을 read로 열기
    words = [word.rstrip() for word in file if isPanlidrome_recursive(word.rstrip())]
    # 문자열을 저장하는데, rstrip 이용해서 linefeed 제거

for i in words:
    print(i, 'is palindrome')
