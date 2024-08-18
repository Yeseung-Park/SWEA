import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    money_dict = {50000: 0, 10000: 0, 5000: 0, 1000: 0,
                  500: 0, 100: 0, 50: 0, 10: 0}    # 돈의 종류별 필요한 개수

    for money in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        while N >= money:
            money_dict[money] += 1
            N -= money

    result = money_dict.values()
    print(f'#{tc}')
    print(*result)