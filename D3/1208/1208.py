import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    boxes = list(map(int, input().split()))

    i = 0    # 실행 횟수

    while i < N:

        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

        if max(boxes)-min(boxes) <= 1:
            break
        else:
            i += 1

    result = max(boxes)-min(boxes)

    print(f'#{tc} {result}')