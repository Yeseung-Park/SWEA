import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    text = input()

    for i in range(1, 11):
        find_pattern = True
        temp = text[:i]
        for j in range(0, i*(30//i-1)+1, i):
            if text[j:j+i] == temp:
                pass
            else:
                find_pattern = False
                break
        if find_pattern == True:
            result = i
            break

    print(f'#{tc} {result}')