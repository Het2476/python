def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def perfect(n):
    if n <= 0:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == n

def palindrome(n):
    return str(n) == str(n)[::-1]

def automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))


number = int(input("Enter a number"))

print(f"Is {number} prime? {prime(number)}")
print(f"Is {number} perfect? {perfect(number)}")
print(f"Is {number} Armstrong? {armstrong(number)}")
print(f"Is {number} palindrome? {palindrome(number)}")
print(f"Is {number} automorphic? {automorphic(number)}")