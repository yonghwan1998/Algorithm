import math

def solution(arr):
    answer = 1
    
    for n in arr:
        answer = math.lcm(answer, n)
    
    return answer