import math

list_input = list(map(int, input().split(', ')))

returnPerimeter = list(map(lambda r: 2 * math.pi * r, list_input))

print(', '.join(f'{x:.2f}'for x in returnPerimeter))