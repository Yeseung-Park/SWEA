import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]
    result = 0

    # 행 먼저 검색
    for i in range(N):
        string = ''.join(puzzle[i])
        temp = string.split('0')
        for box in temp:
            if len(box) == K:
                result += 1

    # 열 검색을 위해 전치행렬 만들기
    for i in range(N):
        for j in range(N):
            if i < j:
                puzzle[i][j], puzzle[j][i] = puzzle[j][i], puzzle[i][j]

    # 열 검색
    for i in range(N):
        string = ''.join(puzzle[i])
        temp = string.split('0')
        for box in temp:
            if len(box) == K:
                result += 1

    print(f'#{tc} {result}')