S = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
list_alphabet = [0] * len(alphabet)

for s in S:
    list_alphabet[alphabet.index((s))] += 1

print(*list_alphabet)