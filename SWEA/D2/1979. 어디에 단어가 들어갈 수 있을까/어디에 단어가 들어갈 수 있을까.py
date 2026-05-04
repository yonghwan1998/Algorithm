T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    temp = list()
    temp2 = [[0] * N for _ in range(N)]
    
    answer = 0
    
    for _ in range(N):
        temp.append(list(map(int, input().split())))
        
    for i in range(N):
        for j in range(N):
            temp2[i][j] = temp[j][i]
    
    for row in temp2:
        temp.append(row)

    count_list = list()
        
    for n in range(N*2):
        cnt = 0
        
        for k in range(N):
            if temp[n][k] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        
        count_list.append(cnt)
        
        if cnt == K:
            answer += 1
    
    print(f"#{test_case} {answer}")