import sys

sys.stdin = open('input.txt')

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, R = map(int, input().split())

    temp = fact(N)//(fact(R)*fact(N-R))
    result = temp % 1234567891

    print(f'#{tc} {result}')