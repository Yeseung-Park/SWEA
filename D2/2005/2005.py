import sys

sys.stdin = open('input.txt')


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def combi(n, i):

    return fact(n)//(fact(i)*fact(n-i))

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    pascal = [[] for _ in range(N)]

    for i in range(N):
        if i == 0:
            pascal[i].append(1)
        else:
            for j in range(i+1):
                pascal[i].append(combi(i, j))

    print(f'#{tc}')
    for number in pascal:
        print(*number)