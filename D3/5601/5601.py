import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = input()
    temp = '1/'+N
    result = []

    for _ in range(int(N)):
        result.append(temp)

    print(f'#{tc}', *result)