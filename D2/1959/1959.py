import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = -1e9

    if N <= M:    # B가 더 길 경우 A를 계속 움직이기
        for i in range(0, M-N+1):
            temp_result = 0
            for j in range(0, N):
                temp = B[i+j]*A[j]
                temp_result += temp
            if temp_result >= result:
                result = temp_result
    else:    # A가 더 길 경우 B를 계속 움직이기
        for i in range(0, N-M+1):
            temp_result = 0
            for j in range(0, M):
                temp = A[i+j]*B[j]
                temp_result += temp
            if temp_result >= result:
                result = temp_result

    print(f'#{tc} {result}')