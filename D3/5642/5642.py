import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    maximum = -1000*N

    for i in range(1, N+1):
        init_sum = 0
        for j in range(i):
            init_sum += numbers[j]
        if init_sum > maximum:
            maximum = init_sum
        for j in range(N-i):
            temp_sum = init_sum + numbers[j+i] - numbers[j]
            if temp_sum > maximum:
                maximum = temp_sum
            init_sum = temp_sum

    print(f'#{tc} {maximum}')