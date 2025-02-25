import random
num = [random.randint(-100, 100) for i in range(30)]
pos = [num for num in num if num > 0]
neg = [num for num in num if num < 0]
print("Random Numbers:", num)
print("Positive Numbers:", pos)
print("Negative Numbers:", neg)