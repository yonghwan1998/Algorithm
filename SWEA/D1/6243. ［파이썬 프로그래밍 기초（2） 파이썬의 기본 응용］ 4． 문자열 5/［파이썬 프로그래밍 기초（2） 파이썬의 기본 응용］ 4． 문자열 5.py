set_input = set(list(map(str, input().split())))

print(*sorted(set_input), sep=',')