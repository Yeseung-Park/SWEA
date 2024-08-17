import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    a, b = map(int, input().split())
    if a > b:
        print(f'#{tc} >')
    elif a == b:
        print(f'#{tc} =')
    else:
        print(f'#{tc} <')