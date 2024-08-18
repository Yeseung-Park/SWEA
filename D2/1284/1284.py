import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    P, Q, R, S, W = map(int, input().split())    # 변수 받아오기

    A = P * W    # A 회사

    # B 회사 가격 구하기
    if W <= R:
        B = Q
    else:
        B = Q + (W-R)*S

    if A >= B:    # B가 더 저렴하면
        result = B    # 결과는 B 회사
    else:    # 그 외에는
        result = A    # 결과는 A 회사

    print(f'#{tc} {result}')