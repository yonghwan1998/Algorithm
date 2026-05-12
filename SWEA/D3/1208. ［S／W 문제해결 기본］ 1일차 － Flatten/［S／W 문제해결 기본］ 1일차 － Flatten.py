for test_case in range(1, 11):
    dump_count = int(input())
    list_box = list(map(int, input().split()))
    
    answer = 0
    
    for _ in range(dump_count):
        max_box = max(list_box)
        min_box = min(list_box)
        
        # 횟수를 채우기 전 평탄화 완료
        if max_box == min_box:
            answer = 0
            break
            
        list_box[list_box.index(max_box)] = max_box - 1
        list_box[list_box.index(min_box)] = min_box + 1
        
        answer = max(list_box) - min(list_box)
    
    print(f"#{test_case} {answer}")