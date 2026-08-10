def solution(topping):
    answer = 0
    
    dict_right = {}
    dict_left = {}
    
    for item in topping:
        dict_right[item] = dict_right.get(item, 0) + 1
        
    for item in topping:
        dict_left[item] = dict_left.get(item, 0) + 1
        dict_right[item] = dict_right.get(item, 0) - 1
        
        if dict_right[item] == 0:
            del dict_right[item]
        
        if len(dict_left.keys()) == len(dict_right.keys()):
            answer += 1
        
    return answer