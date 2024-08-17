import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

N = int(input())    # 주어진 숫자

for i in range(N+1):
    print(2**i, end = ' ')