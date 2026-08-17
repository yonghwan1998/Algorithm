def solution(participant, completion):
    answer = ''
    
    dict_participant = {}
    
    for item in participant:
        dict_participant[item] = dict_participant.get(item, 0) + 1
        
    for item in completion:
        dict_participant[item] = dict_participant[item] - 1
        if not dict_participant[item]:
            del dict_participant[item]
    
    for key in dict_participant.keys():
        answer = key
    return answer