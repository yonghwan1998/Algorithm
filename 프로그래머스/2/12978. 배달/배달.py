def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    distance = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)
    
    distance[1] = 0
    
    for _ in range(N + 1):
        min_distance = float('inf')
        node = -1
        
        for i in range(1, N + 1):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                node = i
                
        if node == -1:
            break
            
        visited[node] = True    
        
        for next_node, weight in graph[node]:
            if not visited[next_node]:
                if distance[next_node] > distance[node] + weight:
                    distance[next_node] = distance[node] + weight
                    
    for time in distance:
        if time <= K:
            answer += 1

    return answer