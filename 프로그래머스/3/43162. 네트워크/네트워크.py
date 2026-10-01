def search(node, computers, visited):
    visited[node] = 1
    
    for i in range(len(computers)):
        if computers[node][i] == 1 and visited[i] == 0:
            search(i, computers, visited)

def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            search(i, computers, visited)
    
    return answer