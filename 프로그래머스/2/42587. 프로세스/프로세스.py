def solution(priorities, location):
    answer = 0
    
    while priorities:
        # 프로세스 꺼내기
        temp = priorities.pop(0)
        
        if priorities and temp < max(priorities):
            # 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣기
            priorities.append(temp)

            # 위치 정보(location)도 프로세스 순서와 함께 이동
            location -= 1
            if location < 0:
                location = len(priorities) - 1
        else:
            # 프로세스가 정상 실행되기에 cnt 증가
            answer += 1
            
            if location == 0:
                break
                
            location -= 1
            
    
    return answer