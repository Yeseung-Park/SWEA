import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())    # 찾아야 하는 회문의 길이
    board = [list(input()) for _ in range(8)]
    result = 0

    # 행 검색
    for i in range(8):
        for j in range(8-N+1):
            temp = board[i][j:j+N]    # N개씩 끊고
            if temp == temp[::-1]:    # 회문이면
                result += 1

    # 열 검색을 위한 전치 행렬
    for i in range(8):
        for j in range(8):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    # 열 검색
    for i in range(8):
        for j in range(8 - N + 1):
            temp = board[i][j:j + N]  # N개씩 끊고
            if temp == temp[::-1]:  # 회문이면
                result += 1

    print(f'#{tc} {result}')