import random

odd = [random.randint(range(1, 100, 2)) for _ in range(5)]
print("List of 5 odd integers:", odd)

even = [random.randint(range(0, 100, 2)) for _ in range(4)]
print("List of 4 even integers:", even)

odd[2] = even
print("List after replacing the third element with even integers:", odd)

fl = [item for sublist in odd for item in (sublist if isinstance(sublist, list) else [sublist])]
print("Flattened list:", fl)

sl = sorted(fl)
print("Sorted list:", sl)