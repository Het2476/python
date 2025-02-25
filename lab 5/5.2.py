import random


r = [random.randint(1, 100) for _ in range(20)]
print("Generated list of random integers:", r)

num = int(input("Enter a number to find its pos in the list: "))

pos = [index for index, value in enumerate(r) if value == num]

if pos:
    print(f"The number {num} is found at pos: {pos}")
else:
    print(f"The number {num} is not found in the list.")