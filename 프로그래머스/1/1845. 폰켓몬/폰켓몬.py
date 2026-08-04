def solution(nums):
    answer = 0
    cnt_n = len(nums) // 2
    cnt_set = len(set(nums))
    
    answer = min(cnt_n, cnt_set)
    return answer