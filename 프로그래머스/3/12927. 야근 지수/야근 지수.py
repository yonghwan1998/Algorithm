import heapq

def solution(n, works):
    answer = 0
    
    # 가지치기
    if sum(works) < n:
        return answer

    # 음수 최대힙
    heap = [-work for work in works]
    heapq.heapify(heap)
    
    # heap에서 가장 작은 값 빼고 1 더해서 넣기
    for _ in range(n):
        max_value = heapq.heappop(heap)
        heapq.heappush(heap, max_value + 1)
    
    answer = sum(work ** 2 for work in heap)
    
    return answer