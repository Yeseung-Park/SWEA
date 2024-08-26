import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())

    board = [list(input()) for _ in range(100)]

    # 가장 긴 것부터 하나씩 줄여나가면서 탐색하면 좀 괜찮지 않을까? 아닌가?
    result = 0

    # 행 별 검색
    for i in range(100):
        find = False
        result_row = 0
        for k in range(100, 0, -1):
            for j in range(0, 100-k+1):
                temp = board[i][j:j+k]
                if temp == temp[::-1]:
                    result_row = k
                    find = True
                    break
            if find:
                break
        if result_row > result:
            result = result_row

    # 열 별 검색을 위한 전치 행렬 만들기
    for i in range(100):
        for j in range(100):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    # 열 별 검색
    for i in range(100):
        find = False
        result_col = 0
        for k in range(100, 0, -1):
            for j in range(0, 100-k+1):
                temp = board[i][j:j+k]
                if temp == temp[::-1]:
                    result_col = k
                    find = True
                    break
            if find:
                break
        if result_col > result:
            result = result_col

    print(f'#{tc} {result}')