def solution(s):
    answer = []
    
    s = s[1:-1]
    
    l = []
    temp = []
    temp_digit = ''
    
    for c in s:
        if c == '{':
            temp = []
        elif c.isdigit():
            temp_digit += c
        elif c == ',':
            if temp_digit:
                temp.append(int(temp_digit))
                temp_digit = ''
        elif c == '}':
            if temp_digit:
                temp.append(int(temp_digit))
                temp_digit = ''
                
            l.append(temp)
    
    # 전부 보면서 길이가 짧은 순서대로 비교
    l.sort(key=len)
    for item in l:
        for i in item:
            if i not in answer:
                answer.append(i)
                continue
    
    return answer