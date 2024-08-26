import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))

    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for i in range(1, N):
        current_sum = max(current_sum + numbers[i], numbers[i])
        maximum_sum = max(maximum_sum, current_sum)

    print(f'#{tc} {maximum_sum}')