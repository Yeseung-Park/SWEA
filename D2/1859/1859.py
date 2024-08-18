# 이건 절대 D2 문제가 아니다

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    prices = list(map(int, input().split()))
    expense = 0

    for i in range(N-1, 0, -1):
        if prices[i] > prices[i-1]:
            expense += prices[i] - prices[i-1]
            prices[i-1] = prices[i]

    print(f'#{tc} {expense}')