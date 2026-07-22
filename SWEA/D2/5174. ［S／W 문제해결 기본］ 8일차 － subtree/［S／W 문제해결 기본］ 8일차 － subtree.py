T = int(input())

def dfs(v):
    cnt = 1
    
    for child in tree[v]:
        cnt += dfs(child)
    
    return cnt

for test_case in range(1, 1 + T):
    E, N = map(int, input().split())
    
    node = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]
    
    for i in range(E):
        parent = node[i * 2]
        child = node[i * 2 + 1]
        tree[parent].append(child)
        
    answer = dfs(N)
    
    print(f"#{test_case} {answer}")