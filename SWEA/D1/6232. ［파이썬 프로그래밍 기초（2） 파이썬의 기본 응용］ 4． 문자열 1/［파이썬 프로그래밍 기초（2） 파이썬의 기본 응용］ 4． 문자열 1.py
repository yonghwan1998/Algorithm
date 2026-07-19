s = input()
s_reversed = "".join(reversed(s))

print(s_reversed)
if s == s_reversed:
    print("입력하신 단어는 회문(Palindrome)입니다.")