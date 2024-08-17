import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    numbers = list(map(int, input().split()))
    result = 0

    for number in numbers:
        if number % 2 == 1:
            result += number

    print(f'#{tc} {result}')