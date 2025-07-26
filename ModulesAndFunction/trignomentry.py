import math

def calculateSinCosTan(x):
    tan = math.tan(math.radians(x))
    sin = math.sin(math.radians(x))
    cos = math.cos(math.radians(x))

    return [sin, cos, tan]

print(calculateSinCosTan(30))
print(calculateSinCosTan(90))