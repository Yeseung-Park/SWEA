# 시간 초과

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    hays = [0]*N

    for i in range(N):
        hays[i] = int(input())

    goal = sum(hays) // N
    dificit = 0

    for hay in hays:
        if hay < goal:
            dificit += goal-hay

    print(f'#{tc} {dificit}')