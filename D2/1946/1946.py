import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    array = [list(input().split()) for _ in range(N)]
    string = ''

    for arr in array:
        string += arr[0]*int(arr[1])    # 압축파일 해제

    i = 0    # 시작 인덱스

    print(f'#{tc}')
    # 10개씩 출력
    for _ in range(len(string)//10):
        print(string[i:i+10])
        i += 10
    print(string[i:])    # 마지막은 그냥 한번에
