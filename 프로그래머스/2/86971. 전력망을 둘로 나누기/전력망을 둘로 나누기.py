def search(node, graph, visited):
    cnt = 1
    visited[node] = 1
    
    for next_node in graph[node]:
        if visited[next_node] == 1:
            continue
            
        cnt += search(next_node, graph, visited)
    
    return cnt

def solution(n, wires):
    answer = 100
    
    for i in range(len(wires)):
        wires_copy = wires.copy()
        wires_copy.pop(i)
        
        graph = [[] for _ in range(n + 1)]
        
        for a, b in wires_copy:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [0] * (n + 1)
        
        cnt = search(1, graph, visited)
        
        answer = min(answer, abs(n - 2 * cnt))
    
    return answer