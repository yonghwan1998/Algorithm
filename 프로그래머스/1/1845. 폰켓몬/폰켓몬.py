def solution(nums):
    answer = 0
    dict_phone = {}
    
    for item in nums:
        dict_phone[item] = True
    
    answer = min(len(dict_phone), len(nums) // 2)
    return answer