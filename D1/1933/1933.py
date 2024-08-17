import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')