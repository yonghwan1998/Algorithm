salt_water = 100
concentration = 20
water = 200

salt = salt_water * concentration / 100
total = salt_water + water

result = salt / total * 100

print(f"혼합된 소금물의 농도: {result:.2f}%")