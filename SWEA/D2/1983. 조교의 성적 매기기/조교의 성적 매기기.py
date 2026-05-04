#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    list_score = list() # 전체 학생 점수 저장
    temp_score = 0 # 찾을 학생의 점수 임시 저장 변수
    
    rating_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    # 각 학생 점수를 list_score에 저장
    for _ in range(N):
        tc_score = list(map(int, input().split()))
        list_score.append(tc_score[0] * 0.35 + tc_score[1] * 0.45 + tc_score[2] * 0.2)
        
    temp_score = list_score[K-1]
    
    list_score.sort(reverse=True) # 전체 학생 점수 내림차순 정렬
    
    rating_cnt = 0 # 평점 index 변수
    for score in list_score:
        if score == temp_score:
            break
        else:
            rating_cnt += 1
            
    answer = rating_list[rating_cnt // (N // 10)]
    print(f"#{test_case} {answer}")