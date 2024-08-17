import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= int(day) <= 31:
            result = f'{year}/{month}/{day}'
        else:
            result = -1
    elif int(month) in [4, 6, 9, 11]:
        if 1 <= int(day) <= 30:
            result = f'{year}/{month}/{day}'
        else:
            result = -1
    elif int(month) == 2:
        if 1 <= int(day) <= 28:
            result = f'{year}/{month}/{day}'
        else:
            result = -1
    else:
        result = -1

    print(f'#{tc} {result}')