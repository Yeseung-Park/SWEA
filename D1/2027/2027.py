import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):

for i in range(5):
    text = ['+', '+', '+', '+', '+']
    text[i] = '#'
    result = ''.join(text)
    print(result)