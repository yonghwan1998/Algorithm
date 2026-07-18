s = input()

cnt_upper = 0
cnt_lower = 0

for c in s:
    if c.isupper():
        cnt_upper += 1
    if c.islower():
        cnt_lower += 1

print(f"UPPER CASE {cnt_upper}")
print(f"LOWER CASE {cnt_lower}")