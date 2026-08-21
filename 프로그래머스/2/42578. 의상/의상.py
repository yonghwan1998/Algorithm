def solution(clothes):
    answer = 0
    
    dict_clothes = {}
    
    for i in clothes:
        dict_clothes[i[1]] = dict_clothes.get(i[1], 0) + 1

    temp = 1
    for cnt in dict_clothes.values():
        temp *= (cnt + 1)
    answer = temp - 1
    
    return answer