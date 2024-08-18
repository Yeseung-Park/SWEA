import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [[0]*N for _ in range(N)]    # 기본 배열 만들기

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]    # 델타 배열
    direction = 0    # 방향을 나타내는 수
    i, j = 0, 0    # 시작 위치

    for num in range(1, N*N+1):
        arr[i][j] = num

        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and arr[i+di[direction]][j+dj[direction]] == 0:
            # 숫자를 넣을 수 있다면 방향 그대로
            pass
        else:    # 막혀있으면 방향전환
            direction = (direction+1) % 4    # 4를 주기로 반복하기 때문에 4의 나머지

        i = i + di[direction]
        j = j + dj[direction]

    print(f'#{tc}')
    for row in arr:
        print(*row)