import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    numbers = set()    # 본 번호들을 담을 set
    i = 0    # 배수 표현

    while len(numbers) != 10:    # 0부터 9까지의 숫자를 다 볼 때까지
        i += 1
        number = N*i    # 셀 양의 수
        number_str = str(number)    # 양의 수를 하나하나 확인하기 위해 문자열로 변환
        for num in number_str:    # 자릿수 하나하나
            numbers.add(num)    # numbers에 넣기

    print(f'#{tc} {number}')
