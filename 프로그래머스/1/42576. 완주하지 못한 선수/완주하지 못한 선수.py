def solution(participant, completion):
    answer = ''
    player_dict = {}
    
    for p in participant:
        player_dict[p] = player_dict.get(p, 0) + 1
    
    for c in completion:
        player_dict[c] -= 1
        
    for k, v in player_dict.items():
        if v == 1:
            answer = k
            break
    
    return answer