def transFtoC(f):
    return (f - 32) * 5 / 9

f = 82

print(f"{f:.2f} ℉ =>  {transFtoC(f):.2f} ℃")