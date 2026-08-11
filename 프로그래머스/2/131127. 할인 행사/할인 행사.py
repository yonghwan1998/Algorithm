def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount) - sum(number) + 1):
        temp_dict = want_dict.copy()
        for j in range(sum(number)):
            temp_dict[discount[i + j]] = temp_dict.get(discount[i + j], 0) - 1
            
            if temp_dict[discount[i + j]] == 0:
                del temp_dict[discount[i + j]]
            
        if not temp_dict:
            answer += 1
    
    return answer