import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    month1, day1, month2, day2 = map(int, input().split())
    result = 0    # 최종 결과를 담을 변수

    if month1 == month2:    # 만약 같은 달 안에서 계산하면
        result += day2-day1+1    # 그냥 계산하기
    else:    # 그 외의 경우
        if month1 in [1, 3, 5, 7, 8, 10, 12]:    # 시작하는 달이 31일 달이라면
            result += 31-day1+1    # 우선 그 달의 일수를 계산하고
            for month in range(month1+1, month2):    # 끝나는 달 사이에 있는 달에 대해
                if month in [4, 6, 9, 11]:    # 30일 달이라면
                    result += 30    # 30 더하기
                elif month == 2:    # 2월이라면
                    result += 28    # 28 더하기
                else:    # 31일 달이라면
                    result += 31    # 31 더하기
            result += day2    # 그 후 끝나는 달의 일수 계산하기
        # 여기서부터는 이하동문
        elif month1 in [4, 6, 9, 11]:
            result += 30 - day1 + 1
            for month in range(month1 + 1, month2):
                if month in [4, 6, 9, 11]:
                    result += 30
                elif month == 2:
                    result += 28
                else:
                    result += 31
            result += day2
        else:
            result += 28 - day1 + 1
            for month in range(month1 + 1, month2):
                if month in [4, 6, 9, 11]:
                    result += 30
                elif month == 2:
                    result += 28
                else:
                    result += 31
            result += day2

    print(f'#{tc} {result}')