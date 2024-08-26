import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())
    password = list(map(int, input().split()))

    while password[-1] != 0:
        for i in range(1, 6):
            password[0] -= i
            if password[0] < 0:
                password[0] = 0
            password.append(password[0])
            password.pop(0)
            if password[-1] == 0:
                break

    print(f'#{tc}', *password)