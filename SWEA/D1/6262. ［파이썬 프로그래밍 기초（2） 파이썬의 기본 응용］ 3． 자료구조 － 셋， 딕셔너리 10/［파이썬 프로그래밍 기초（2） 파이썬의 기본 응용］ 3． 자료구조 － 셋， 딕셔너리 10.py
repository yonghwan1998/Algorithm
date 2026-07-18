s = input()
dic_s = {}

for c in s:
    if c in dic_s:
        dic_s[c] += 1
    else:
        dic_s[c] = 1
        
for k, v in dic_s.items():
    print(k, v, sep=',')