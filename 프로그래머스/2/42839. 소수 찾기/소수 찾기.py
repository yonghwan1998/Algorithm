from itertools import permutations

def solution(numbers):
    answer = 0
    
    digits = list(map(int, numbers))
    all_numbers = set()
    
    for r in range(1, len(digits) + 1):
        for p in permutations(digits, r):
            num = int("".join(map(str, p)))
            all_numbers.add(num)
    
    for number in all_numbers:
        if number < 2:
            continue
            
        is_prime_number = True
        
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime_number = False
                break
                
        if is_prime_number:
            answer += 1
    
    return answer