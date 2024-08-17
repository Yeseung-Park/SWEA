import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    numbers = list(map(int, input().split()))
    sum_num = sum(numbers)
    n = len(numbers)

    result = round(sum_num / n)

    print(f'#{tc} {result}')