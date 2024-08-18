import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += flies[i+k][j+l]
            if temp > maximum:
                maximum = temp

    print(f'#{tc} {maximum}')