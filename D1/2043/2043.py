import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

P, K = map(int, input().split())
count = 0

while K != P+1:
    K += 1
    count += 1

print(count)