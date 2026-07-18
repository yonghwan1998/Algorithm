user_a = input()
user_b = input()

hand_a = input()
hand_b = input()

def battle(hand_a, hand_b):
    if (hand_a == '가위' and hand_b == '바위') or (hand_a == '바위' and hand_b == '가위'):
        print('바위가 이겼습니다!')
    if (hand_a == '바위' and hand_b == '보') or (hand_a == '보' and hand_b == '바위'):
        print('보가 이겼습니다!')
    if (hand_a == '보' and hand_b == '가위') or (hand_a == '가위' and hand_b == '보'):
        print('가위가 이겼습니다!')
        
battle(hand_a, hand_b)