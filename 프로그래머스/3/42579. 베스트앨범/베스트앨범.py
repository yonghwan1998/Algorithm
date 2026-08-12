def solution(genres, plays):
    answer = []
    
    dict_best = {}
    
    for i in range(len(plays)):
        dict_best[genres[i]] = dict_best.get(genres[i], 0) + plays[i]
        
    dict_best_sorted = dict(sorted(dict_best.items(), key=lambda x: x[1], reverse=True))
    
    for k, v in dict_best_sorted.items():
        dict_idx = {}
        
        for i in range(len(plays)):
            if genres[i] == k:
                dict_idx[i] = plays[i]
    
        dict_idx_sorted = dict(sorted(dict_idx.items(), key=lambda x: x[1], reverse=True))
        
        cnt = 0
        for k in dict_idx_sorted.keys():
            answer.append(k)
            
            cnt += 1
            if cnt == 2:
                break
                
    return answer