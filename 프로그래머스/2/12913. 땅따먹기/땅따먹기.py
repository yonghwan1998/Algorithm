def solution(land):
    answer = 0
    length = len(land)
    
    dp = [[0] * 4 for _ in range(length)]
    
    dp[0] = land[0]
    
    for row in range(1, length):
        for col in range(4):
            for i in range(4):
                if i == col:
                    continue
                
                dp[row][i] = max(dp[row][i], dp[row - 1][col] + land[row][i])
                
    answer = max(dp[length - 1])

    return answer