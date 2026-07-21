T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    answer = []
    
    cnt = abs(N - M) + 1
    
    for i in range(cnt):
        temp = 0
        
        if N < M:
            for index in range(N):
                temp += A[index] * B[index + i]
        elif N > M:
            for index in range(M):
                temp += A[index + i] * B[index]
        answer.append(temp)
        
    print(f"#{test_case} {max(answer)}")