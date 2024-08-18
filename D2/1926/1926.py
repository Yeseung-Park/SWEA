import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

N = int(input())

for i in range(1, N+1):
    temp = str(i)
    count_3 = temp.count('3')
    count_6 = temp.count('6')
    count_9 = temp.count('9')
    total_count = count_3 + count_6 + count_9
    if total_count != 0:
        print('-'*total_count, end=' ')
    else:
        print(temp, end=' ')