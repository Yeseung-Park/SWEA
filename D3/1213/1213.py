import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())
    pattern = input()
    text = input()
    i = 0    # 탐색을 시작할 인덱스
    count = 0    # 문자열이 등장하는 횟수

    while i < len(text):    # 인덱스가 text의 인덱스를 벗어나기 전까지
        if text[i:i+len(pattern)] == pattern:    # 만약 pattern이랑 문자열이 일치하면
            count += 1    # 횟수 추가하고
            i += len(pattern)    # pattern 길이만큼 건너뛰어서 탐색 다시 시작
        else:    # 그 외의 경우에는
            i += 1    # 인덱스 하나만 추가하기

    print(f'#{tc} {count}')