c = input()

if c.isupper():
    print(f"{c}(ASCII: {ord(c)}) => {c.lower()}(ASCII: {ord(c.lower())})")
elif c.islower():
    print(f"{c}(ASCII: {ord(c)}) => {c.upper()}(ASCII: {ord(c.upper())})")
else:
    print(c)