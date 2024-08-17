import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

A, B = map(int, input().split())

if (A == 2 and B == 1) or (A == 3 and B == 2) or (A == 1 and B == 3):
    print('A')
else:
    print('B')