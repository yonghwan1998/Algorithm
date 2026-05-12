for test_case in range(1, 11):
    answer = 0
    
    N = int(input())
    list_building = list(map(int, input().split()))
    
    for i in range(2, N-2):
        height_center = list_building[i] # 가운데 빌딩의 높이
        height_max = max(max(list_building[i-2:i]), max(list_building[i+1:i+3])) # 좌우 2개씩 중 가장 높은 빌딩의 높이
        
        # 좌우 2개보다 가운데 빌딩의 높이가 제일 높다면
        if height_center > height_max:
            answer += (height_center - height_max) # 차이만큼 더하기
        
    print(f"#{test_case} {answer}")