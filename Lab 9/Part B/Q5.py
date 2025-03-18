# Calculate ab where a and b received through the keyword using recursion.

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(power(a, b))
a