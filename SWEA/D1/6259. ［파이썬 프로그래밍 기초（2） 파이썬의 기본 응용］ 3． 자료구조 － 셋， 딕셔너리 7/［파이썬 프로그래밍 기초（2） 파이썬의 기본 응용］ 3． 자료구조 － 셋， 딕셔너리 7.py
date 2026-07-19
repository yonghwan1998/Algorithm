s = input()
cnt_letters = 0
cnt_digits = 0

for c in s:
    if c.isalpha():
        cnt_letters += 1
    if c.isdecimal():
        cnt_digits += 1
        
print(f"LETTERS {cnt_letters}")
print(f"DIGITS {cnt_digits}")