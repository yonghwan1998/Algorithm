T = int(input())

def bfs(start):
    queue.append(start)
    distance[start] = 0
    
    while queue:
        now = queue.pop(0)
        
        if now == G:
            break
        
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)
    
for test_case in range(1, 1 + T):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    S, G = map(int, input().split())
    
    queue = []
    distance = [-1] * (V + 1)
    bfs(S)
    
    answer = distance[G]
    
    if answer == -1:
        answer = 0
    
    print(f"#{test_case} {answer}")