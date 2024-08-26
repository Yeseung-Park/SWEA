import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    buildings = list(map(int, input().split()))
    view_fine = True
    view = 0

    for i in range(2, N-2):
        minimum = 1e9
        temps = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
        for temp in temps:
            if buildings[i]-temp < minimum:
                minimum = buildings[i]-temp
        if minimum < 0:
            pass
        else:
            view += minimum

    print(f'#{tc} {view}')