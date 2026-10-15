def solution(n):
    bin_n = str(bin(n)[2:])
    cnt_n = len(bin_n.replace('0', ''))
    
    target = n
    cnt_target = -1
    
    while cnt_n != cnt_target:
        target += 1
        bin_target = str(bin(target)[2:])
        cnt_target = len(bin_target.replace('0', ''))
    
    return target