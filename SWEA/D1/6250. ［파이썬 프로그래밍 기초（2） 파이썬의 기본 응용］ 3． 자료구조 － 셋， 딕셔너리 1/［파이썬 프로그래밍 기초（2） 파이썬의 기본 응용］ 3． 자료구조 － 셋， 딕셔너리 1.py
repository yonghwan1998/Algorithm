battle_dict = {"가위": 1, "바위":2, "보": 3}

A = input()
B = input()

if battle_dict.get(A) == 1:
    if battle_dict.get(B) == 1:
        print("비겼습니다.")
    elif battle_dict.get(B) == 2:
        print("Player B가 이겼습니다.")
    elif battle_dict.get(B) == 3:
        print("Player A가 이겼습니다.")
elif battle_dict.get(A) == 2:
    if battle_dict.get(B) == 1:
        print("Player A가 이겼습니다.")
    elif battle_dict.get(B) == 2:
        print("비겼습니다.")
    elif battle_dict.get(B) == 3:
        print("Player B가 이겼습니다.")
elif battle_dict.get(A) == 3:
    if battle_dict.get(B) == 1:
        print("Player B가 이겼습니다.")
    elif battle_dict.get(B) == 2:
        print("Player A가 이겼습니다.")
    elif battle_dict.get(B) == 3:
        print("비겼습니다.")
        
print("게임을 계속 진행하겠습니까? (예/아니오)")