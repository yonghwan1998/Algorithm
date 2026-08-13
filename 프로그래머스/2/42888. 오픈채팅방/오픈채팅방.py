def solution(record):
    answer = []
    
    dict_uid = {}

    for item in record:
        input = list(map(str, item.split()))
        
        if len(input) == 3:
            dict_uid[input[1]] = input[2]
            
    for item in record:
        input = list(map(str, item.split()))
        action = input[0]
        uid = input[1]
        
        if action == 'Enter':
            answer.append(f'{dict_uid[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{dict_uid[uid]}님이 나갔습니다.')
    
    return answer