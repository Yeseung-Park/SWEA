import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]

    maximum = -1e9

    # 행 먼저 검색
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += numbers[i][j]
        if temp > maximum:
            maximum = temp

    # 열 다음 검색
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += numbers[i][j]
        if temp > maximum:
            maximum = temp

    # 오른쪽 아래 대각선 검색
    temp = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                temp += numbers[i][j]
    if temp > maximum:
        maximum = temp

    # 왼쪽 아래 대각선 검색
    temp = 0
    for i in range(100):
        for j in range(100):
            if i == 99-j:
                temp += numbers[i][j]
    if temp > maximum:
        maximum = temp

    print(f'#{tc} {maximum}')