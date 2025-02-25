def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

n = int(input("Enter the value of n"))
r = int(input("Enter the value of r"))
print(f"{n}C{r} = {nCr(n, r)}")
print(f"{n}P{r} = {nPr(n, r)}")