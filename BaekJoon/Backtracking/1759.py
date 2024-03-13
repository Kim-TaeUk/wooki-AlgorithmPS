import sys


def func(K, start):
    if K == L:
        vowel_cnt = sum(1 for char in arr if char in vowels)
        consonant_cnt = L - vowel_cnt
        if vowel_cnt < 1 or consonant_cnt < 2:
            return
        print("".join(map(str, arr)))
        return

    for idx, x in lst[start - 1:]:
        if not is_used[idx]:
            is_used[idx] = True
            arr[K] = x
            func(K + 1, idx + 1)
            is_used[idx] = False


L, C = map(int, sys.stdin.readline().split())
lst = sorted(list(map(str, sys.stdin.readline().split())))
lst = list(enumerate(lst))
vowels = ['a', 'e', 'i', 'o', 'u']
arr = [''] * L
is_used = [False] * (C + 1)
func(0, 1)
