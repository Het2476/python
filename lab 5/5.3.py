import random

num = [random.randint(1, 30) for _ in range(50)]

un = list(set(num))

print(un)