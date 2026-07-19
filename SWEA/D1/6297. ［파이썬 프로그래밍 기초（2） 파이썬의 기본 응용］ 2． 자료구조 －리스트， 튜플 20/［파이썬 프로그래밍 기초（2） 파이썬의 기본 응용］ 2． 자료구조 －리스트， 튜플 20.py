list_input = list(map(int, input().split(', ')))

answer = [odd for odd in list_input if odd % 2 == 1]

print(*answer, sep=', ')