def solution(triangle):
    dp = []
    
    for height in range(len(triangle)):
        temp = []
        
        if height == 0:
            dp.append(triangle[0])
        elif height == 1:
            temp.append(triangle[0][0] + triangle[1][0])
            temp.append(triangle[0][0] + triangle[1][1])
            dp.append(temp)
        else:
            for i in range(height + 1):
                if i == 0:
                    temp.append(dp[height - 1][0] + triangle[height][0])
                elif i == height:
                    temp.append(dp[height - 1][i - 1] + triangle[height][i])
                else:
                    temp.append(max(dp[height - 1][i - 1], dp[height - 1][i]) + triangle[height][i])
            dp.append(temp)
    
    return max(dp[-1])