import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    h1, m1, h2, m2 = map(int, input().split())

    result_h = h1 + h2
    result_m = m1 + m2

    if result_m >= 60:
        result_h += result_m // 60
        result_m = result_m % 60

    if result_h > 12:
        result_h -= 12

    print(f'#{tc} {result_h} {result_m}')