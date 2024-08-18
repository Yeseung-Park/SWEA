import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    test_case = int(input())    # 테스트 케이스 번호
    scores = list(map(int, input().split()))    # 점수 리스트

    num_count = {}    # 점수와 해당 값의 빈도수를 저장할 딕셔너리

    for score in scores:    # 점수에 대해서
        if score in num_count.keys():    # 점수가 딕셔너리의 키로 이미 있다면
            num_count[score] += 1    # 값에 하나 더하기
        else:    # 점수가 딕셔너리의 키로 없다면
            num_count[score] = 0    # 추가하고
            num_count[score] += 1    # 값에 하나 더하기

    mode = max(num_count.values())    # value 중 가장 큰 값이 최빈값
    temp = []    # 최빈값에 해당하는 점수들을 담는 리스트

    for key, value in num_count.items():    # num_count의 키와 값에 대해서
        if value == mode:    # 값이 최빈값이면
            temp.append(key)    # 키를 temp에 append

    result = max(temp)    # temp에서 제일 큰 값이 결과

    print(f'#{test_case} {result}')
