a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

a_keys = [k for k in a.keys()]
b_keys = [k for k in b.keys()]
a_b_keys = list(set(a_keys + b_keys))

a_b_dict = {}

for k in a_b_keys:
    a_b_dict[k] = a.get(k, b.get(k))
    
filtered_set = {(k, v) for k, v in a_b_dict.items() if v >= 3000}

print(filtered_set)