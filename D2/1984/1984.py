import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    numbers = list(map(int, input().split()))

    numbers.sort()

    result = round(sum(numbers[1:-1]) / 8)

    print(f'#{tc} {result}')