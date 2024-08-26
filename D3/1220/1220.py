import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for j in range(100):
        temp = []
        for i in range(100):
            if table[i][j] != 0:
                temp.append(table[i][j])
        i = 0
        while i < len(temp)-1:
            if temp[i] == 1:
                if temp[i+1] == 2:
                    result += 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1

    print(f'#{tc} {result}')