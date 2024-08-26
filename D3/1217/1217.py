import sys

sys.stdin = open('input.txt')

def exp(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*exp(base, exponent-1)

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())
    N, M = map(int, input().split())

    print(f'#{tc}', exp(N, M))

