def transKgToLb(kg):
    return kg * 2.2046

kg = int(input())

print(f"{kg:.2f} kg =>  {transKgToLb(kg):.2f} lb")