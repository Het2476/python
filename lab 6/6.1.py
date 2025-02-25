def cnt(nlist):
    boys = 0
    girls = 0
    for i in nlist:
        if isinstance(i, tuple):
            lenn = len(i)
            boys = boys+lenn
        else:
            girls += 1
    return boys, girls

names = [("Divy","Prayag"), "Nisha", ("Raju",), "priya", ("Tom",), "Jennie"]
boys, girls = cnt(names)
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")