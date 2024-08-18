import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_right = True    # 스도쿠가 맞는지 들린지 확인하는 과정

    # 행 먼저 판별
    if sudoku_right:
        for i in range(9):
            temp = set()
            for j in range(9):
                temp.add(sudoku[i][j])
            if len(temp) != 9:
                sudoku_right = False
                break

    # 그 다음 열 판별
    if sudoku_right:
        for j in range(9):
            temp = set()
            for i in range(9):
                temp.add(sudoku[i][j])
            if len(temp) != 9:
                sudoku_right = False
                break

    # 그 다음 상자 판별
    di = [0, 0, 0, 1, 2, 1, 2, 1, 2]
    dj = [0, 1, 2, 0, 0, 1, 2, 2, 1] # 인접 원소 탐색을 위한 델타 배열
    if sudoku_right:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = set()
                for k in range(9):
                    temp.add(sudoku[i+di[k]][j+dj[k]])
                if len(temp) != 9:
                    sudoku_right = False
                    break

    if sudoku_right:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')