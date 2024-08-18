import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0

    while N % 2 == 0:    # 2로 나누어 떨어지는 동안
        a += 1
        N = N//2

    while N % 3 == 0:    # 3으로 나누어 떨어지는 동안
        b += 1
        N = N//3

    while N % 5 == 0:    # 5로 나누어 떨어지는 동안
        c += 1
        N = N//5

    while N % 7 == 0:    # 7로 나누어 떨어지는 동안
        d += 1
        N = N//7

    while N % 11 == 0:    # 11로 나누어 떨어지는 동안
        e += 1
        N = N//11

    print(f'#{tc}', a, b, c, d, e)