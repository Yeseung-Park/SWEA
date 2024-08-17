import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

N = list(map(int, input()))
result = 0

for num in N:
    result += num

print(result)