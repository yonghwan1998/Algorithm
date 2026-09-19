T = int(input())

def insert_preorder(idx):
    global cnt

    if idx * 2 <= N and tree[idx * 2] == 0:
        insert_preorder(idx * 2)

    tree[idx] = cnt
    cnt += 1

    if idx * 2 + 1 <= N and tree[idx * 2 + 1] == 0:
        insert_preorder(idx * 2 + 1)

for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1

    insert_preorder(1)

    print(f'#{test_case} {tree[1]} {tree[N // 2]}')