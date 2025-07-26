def MathOp():
    modulus = 3 % 2
    divison = 3 / 2
    floorDivision = 3 // 2
    power = 3 ** 2
    return [modulus, divison, floorDivision, power]

[modulus, divison, floorDivision, power] = MathOp()

print(modulus)
print(divison)
print(floorDivision)
print(power)