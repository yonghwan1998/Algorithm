input_dic = {"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}
reversed_dic = {v: k for k, v in input_dic.items()}

temp = [v for v in input_dic.values()]
temp.sort(reverse=True)

temp = list(input_dic.values())
temp.sort(reverse=True)

for price in temp:
    print(f"{reversed_dic[price]}: {price}")