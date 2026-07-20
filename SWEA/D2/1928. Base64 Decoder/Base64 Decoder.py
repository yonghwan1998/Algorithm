T = int(input())

decoder = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for test_case in range(1, 1 + T):
    s = input()
    decoded_full = ""
    answer = ""
    
    for c in s:
        c_decoded = decoder.index(c)
        c_trans_6bit = bin(c_decoded)[2:].zfill(6)
        decoded_full += c_trans_6bit
        
    for i in range(len(decoded_full) // 8):
        bits = int(decoded_full[i * 8: (i + 1) * 8], 2)
        answer += chr(bits)
        
    print(f"#{test_case} {answer}")