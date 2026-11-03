def solution(cacheSize, cities):
    answer = 0
    
    q = []
    
    for city in cities:
        
        city = city.lower()
        
        if city in q:
            answer += 1
            q.append(q.pop(q.index(city)))

        if city not in q:
            answer += 5
            
            if cacheSize != 0:
                if len(q) < cacheSize:
                    q.append(city)
                elif len(q) == cacheSize:
                    q.pop(0)
                    q.append(city)

    return answer