def solution(clothes):
    answer = 0
    
    dict_clothes = {}
    
    for k, v in clothes:
        dict_clothes[v] = dict_clothes.get(v, 0) + 1
        
    temp = 1
    for v in dict_clothes.values():
        temp *= (v + 1)
        
    answer = temp - 1
        
    return answer