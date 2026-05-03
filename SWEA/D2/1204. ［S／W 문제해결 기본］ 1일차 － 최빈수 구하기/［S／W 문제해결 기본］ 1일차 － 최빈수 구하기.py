T = int(input())

for test_case in range(1, T + 1):
    tc_number = int(input())
    tc_score = list(map(int, input().split()))

    # 배열 101개 만들기
    score_storage = [0] * 101
    
    for score in tc_score:
        score_storage[score] += 1
    
    max_count = max(score_storage)
    answer = 0
    
    for i in range(101):
        if score_storage[i] == max_count:
            answer = i

    # 가장 큰 수의 index 반환
    print(f"#{tc_number} {answer}")