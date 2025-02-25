food_items = [
    ("Pizza", 1.50),
    ("Burger", 0.75),
    ("Cherry", 2.00),
    ("Cake", 1.25),
    ("Nachos", 3.00)
]
sortedlist = sorted(food_items, key=lambda item: item[1], reverse=True)

print(sortedlist)