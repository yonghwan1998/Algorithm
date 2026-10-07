import heapq

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    answer_list = []
    
    N = int(input())
    arr = list(map(int, input().split()))

    heap = []
    
    for n in arr:
        heapq.heappush(heap, n)
        
    heap.insert(0, 0)
    node = (len(heap) - 1) // 2
    
    while node > 0:
        answer_list.append(heap[node])
        node = node // 2

    answer = sum(answer_list)
    
    print(f'#{test_case} {answer}')