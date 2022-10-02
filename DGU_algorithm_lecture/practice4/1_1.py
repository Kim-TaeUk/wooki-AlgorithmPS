# 2018112034 김태욱
# /Users/kimtaeuk/Desktop/3-2/알골/실습/4주차/example.txt
def isPanlidrome_iterative(word):
    is_palindrome = True  # 일단 is_palindrome을 True로 설정
    for i in range(len(word) // 2):  # for문을 도는데 문자열 길이의 반만큼 반복한다
        if word[i] != word[-(i + 1)]:  # 앞문자와 뒷문자를 비교하여, 파이썬은 인덱스를 음수 표현해서 끝에서부터 접근이 가능
            is_palindrome = False  # 다르면 False로 is_palindrome으로 바꾸고
            break  # 반복문 탈출
    if is_palindrome:  # 이후 출력해주기
        print(word + ' is palindrome')
    else:
        print(word + ' is NOT palindorme')


with open("/Users/kimtaeuk/Desktop/3-2/알골/실습/4주차/example.txt", 'r') as file:  # 경로의 파일을 read로 열기
    words = [word.rstrip() for word in file if isPanlidrome_iterative(word.rstrip())]
    # 문자열을 저장하는데, rstrip 이용해서 linefeed 제거
