import math

def sin(x, terms=10):
    sine = 0
    for n in range(terms):
        sign = (-1) ** n
        sine += (sign * (x ** (2 * n + 1))) / math.factorial(2 * n + 1)
    return sine

# Convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

# Example usage
degrees = 30
radians = degrees_to_radians(degrees)
print(f"sin({degrees} degrees) = {sin(radians)}")