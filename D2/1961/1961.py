import copy
import sys

sys.stdin = open('input.txt')

def turn_90(list, N):
    # 전치 만들어주고
    for i in range(N):
        for j in range(N):
            if i < j:
                list[i][j], list[j][i] = list[j][i], list[i][j]
    # 좌우 뒤집기
    for i in range(N):
        for j in range(N//2):
            list[i][j], list[i][-1-j] = list[i][-1-j], list[i][j]
    return

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    arr_90 = copy.deepcopy(arr)
    turn_90(arr_90, N)
    arr_180 = copy.deepcopy(arr_90)
    turn_90(arr_180, N)
    arr_270 = copy.deepcopy(arr_180)
    turn_90(arr_270, N)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), end=' ')
        print(''.join(arr_180[i]), end=' ')
        print(''.join(arr_270[i]))