def triplets(max):
    triplets = []
    for i in range(1, max + 1):
        for j in range(i, max + 1):
            c = (i**2 + j**2) ** 0.5
            if c.is_integer() and c <= max:
                triplets.append([i, j, int(c)])
    return triplets

max = 30
triplets = triplets(max)
for triplet in triplets:
    print(triplet)