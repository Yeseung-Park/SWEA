import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # command의 수
    commands = [list(map(int, input().split())) for _ in range(N)]    # command 모음
    result = 0    # 최종 거리를 담는 변수
    velocity = 0    # 속도 변수

    for command in commands:    # 각 command에 대해서
        if command == [0]:    # 가속 감속이 없다면
            result += velocity    # 이전 속도 그대로 반영
        else:    # 그 외의 경우
            if command[0] == 1:    # 가속일 경우
                velocity += command[1]    # 속도에 가속도 추가하고
                result += velocity    # 새로운 속도로 반영
            else:    # 감속일 경우
                velocity -= command[1]    # 속도에 가속도만큼 감소하고
                if velocity < 0:    # 속도가 0보다 작아질 경우
                    velocity = 0    # 그냥 0으로 처리
                result += velocity    # 새로운 속도로 반영

    print(f'#{tc} {result}')