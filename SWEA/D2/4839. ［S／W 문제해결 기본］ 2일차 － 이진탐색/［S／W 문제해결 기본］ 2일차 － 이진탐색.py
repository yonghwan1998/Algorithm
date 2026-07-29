T = int(input())

def binary_search(l, r, target, cnt):
    if l > r:
        return
        
    c = int((l + r) / 2)
    if c == target:
        return cnt
    elif c < target:
        cnt += 1
        return binary_search(c, r, target, cnt)
    else:
        cnt += 1
        return binary_search(l, c, target, cnt)

for test_case in range(1, 1 + T):
    answer = -1
    P, A, B = map(int, input().split())
    
    cnt_a = binary_search(1, P, A, 0)
    cnt_b = binary_search(1, P, B, 0)
    
    if cnt_a < cnt_b:
        answer = 'A'
    elif cnt_b < cnt_a:
        answer = 'B'
    elif cnt_a == cnt_b:
        answer = 0
    
    print(f"#{test_case} {answer}")