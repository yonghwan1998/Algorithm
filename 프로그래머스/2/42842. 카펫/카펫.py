import math

def get_divisor_pairs(n):
    pairs = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            pairs.append([n // i, i])
            
    return pairs

def solution(brown, yellow):
    answer = []
    
    count = brown + yellow
    pairs = get_divisor_pairs(count)
    
    for pair in pairs:
        w_cnt, h_cnt = pair
        
        if (w_cnt * 2 + (h_cnt - 2) * 2) == brown:
            answer = pair
            break
    
    return answer