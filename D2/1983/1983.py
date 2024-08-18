import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    final_scores = [0]*N

    for i in range(N):
        final_score = scores[i][0]*0.35 + scores[i][1]*0.45 + scores[i][2]*0.2
        final_scores[i] = final_score

    K_student = final_scores[K-1]

    final_scores.sort(reverse=True)    # 내림차순으로 정렬
    GPA = {'A+': [], 'A0': [], 'A-': [], 'B+': [],
           'B0': [], 'B-': [], 'C+': [], 'C0': [],
           'C-': [], 'D0': []}    # 평점과 점수를 담는 딕셔너리

    # 진짜 엄청난 하드코딩이다..
    for score in final_scores:
        if final_scores.index(score) < N//10:
            GPA['A+'].append(score)
        elif (N//10)*2 > final_scores.index(score) >= N//10:
            GPA['A0'].append(score)
        elif (N//10)*3 > final_scores.index(score) >= (N//10)*2:
            GPA['A-'].append(score)
        elif (N//10)*4 > final_scores.index(score) >= (N//10)*3:
            GPA['B+'].append(score)
        elif (N//10)*5 > final_scores.index(score) >= (N//10)*4:
            GPA['B0'].append(score)
        elif (N//10)*6 > final_scores.index(score) >= (N//10)*5:
            GPA['B-'].append(score)
        elif (N//10)*7 > final_scores.index(score) >= (N//10)*6:
            GPA['C+'].append(score)
        elif (N//10)*8 > final_scores.index(score) >= (N//10)*7:
            GPA['C0'].append(score)
        elif (N//10)*9 > final_scores.index(score) >= (N//10)*8:
            GPA['C-'].append(score)
        else:
            GPA['D0'].append(score)

    for key, value in GPA.items():
        if K_student in value:
            result = key

    print(f'#{tc} {result}')