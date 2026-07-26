T = int(input())

def dfs(node):
    global answer
    
    if visited[node] == False:
        visited[node] = True
        
    for n in graph[node]:
        dfs(n)
        
    if node == G:
        answer = 1
        return

for test_case in range(1, 1 + T):
    V, E = map(int, input().split())
    answer = 0
    
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        
    S, G = map(int, input().split())
    visited = [False] * (V + 1)
    
    dfs(S)
    
    print(f"#{test_case} {answer}")