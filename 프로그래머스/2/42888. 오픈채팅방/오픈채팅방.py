def solution(record):
    answer = []
    
    dict_nicknames = {}
    
    for item in record:
        parts = item.split()
        
        if parts[0] in {'Enter', 'Change'}:
            dict_nicknames[parts[1]] = parts[2]

    for item in record:
        parts = item.split()
        
        if parts[0] == 'Enter':
            answer.append(f'{dict_nicknames[parts[1]]}님이 들어왔습니다.')
        elif parts[0] == 'Leave':
            answer.append(f'{dict_nicknames[parts[1]]}님이 나갔습니다.')
    
    return answer