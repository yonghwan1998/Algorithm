def solution(s):
    answer = ''
    
    list_s = s.split(' ')
    store = []
    
    for string in list_s:
        if not string:
            store.append('')
            continue
            
        temp = string[0].upper() + string[1:].lower()
        store.append(temp)
    
    answer = ' '.join(store)

    return answer