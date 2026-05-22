N = int(input())

list_number = list(map(int, input().split()))
list_number.sort()

answer = list_number[N // 2]

print(answer)