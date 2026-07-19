def transInchToCm(inch):
    return inch * 2.54

inch = int(input())

print(f"{inch:.2f} inch =>  {transInchToCm(inch):.2f} cm")