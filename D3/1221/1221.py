import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    ignore = input()
    text = list(input().split())

    num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
                'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    num_dict_reverse = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
                        5: 'FIV', 6: 'SIX', 7:'SVN', 8: 'EGT', 9: 'NIN'}

    for i in range(len(text)):
        text[i] = num_dict[text[i]]

    text.sort()

    for i in range(len(text)):
        text[i] = num_dict_reverse[text[i]]

    print(f'#{tc}')
    print(*text)