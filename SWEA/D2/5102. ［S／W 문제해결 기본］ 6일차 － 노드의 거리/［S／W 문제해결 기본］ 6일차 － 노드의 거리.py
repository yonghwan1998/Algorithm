T = int(input())

def bfs(start):
    distance[start] = 0
    queue.append(start)
    
    while queue:
        now = queue.pop(0)
        
        if now == G:
            break
        
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

for test_case in range(1, 1 + T):
    answer = 0
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    queue = []
    distance = [-1] * (V + 1)
    
    for _ in range(E):
        node_1, node_2 = map(int, input().split())
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)
    
    S, G = map(int, input().split())
    
    bfs(S)
    
    answer = distance[G]
    
    if answer == -1:
        answer = 0
    print(f"#{test_case} {answer}")