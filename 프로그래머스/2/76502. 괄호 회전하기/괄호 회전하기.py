def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        stack = []
        
        for c in s:
            if c in '[{(':
                stack.append(c)
            else:
                if not stack:
                    break
                
                c_pop = stack.pop()
                
                if ((c_pop == '[' and c != ']') or (c_pop == '{' and c != '}') or (c_pop == '(' and c != ')')):
                    break
        else:
            if not stack:
                answer += 1
                        
        s = s[1:] + s[0]
            
    return answer