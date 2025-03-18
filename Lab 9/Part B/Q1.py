# If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number.

def prime_factors(n, i=2):
    if n == 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n//i, i)
    return prime_factors(n, i+1)


n = int(input("Enter a number: "))
print(prime_factors(n))
