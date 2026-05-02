T = int(input())

# 2 2 1
# 4 2
for test_case in range(1, T + 1):
    # N명의 사람이 받음 == len(tc_customer)
    # M초의 시간을 들여
    # K개의 붕어빵을 만듦
    N, M, K = list(map(int, input().split())) # N=2, M=2, K=1
    tc_customer = list(map(int, input().split())) #[4, 2]
    
    # 각 손님 도착 시간 오름차순 정렬
    tc_customer.sort() # [2, 4]
    
    possible = True

    # 손님 도착 시간까지 몇개가 만들어졌는지?
    # 해당 시간까지 손님이 몇명 도착했는지?
    for i in range(N):
        # 각 손님 도착 시간 [2, 4]에
        # 만들어진 붕어빵 개수
        made_fish = (tc_customer[i] // M) * K
        visit_customer = i + 1 # 도착한 손님의 수
        
        if made_fish < visit_customer:
            possible = False
            break
        
    if possible:
        print(f"#{test_case} Possible")
    else: 
        print(f"#{test_case} Impossible")