fruit = ['   apple    ','banana','  melon']
answer = {}

for item in fruit:
    item_rm_sp = item.replace(" ", "")
    item_len = len(item_rm_sp)
    
    answer[item_rm_sp] = item_len
    
print(answer)