def solution(clothes):
    answer = 0
    hash_dict = {}
    
    for k, v in clothes:
        hash_dict[v] = hash_dict.get(v, 0) + 1
        
    temp = 1        
    for cnt in hash_dict.values():
        temp *= (cnt + 1)
    
    answer = temp - 1
        
    return answer