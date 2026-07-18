N = int(input())
list_divisor = [i for i in range(1, N + 1) if N % i == 0]
list_divisor.sort
print(*list_divisor)