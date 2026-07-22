T = int(input())

def inorder(v):
    global num
    
    if v > N:
        return
    
    inorder(v * 2)
    tree[v] = num
    
    num += 1
    
    inorder(v * 2 + 1)

for test_case in range(1, 1 + T):
    N = int(input())
    
    tree = [0] * (N + 1)
    num = 1
    
    inorder(1)
    
    print(f"#{test_case} {tree[1]} {tree[N // 2]}")