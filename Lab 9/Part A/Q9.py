# Write a program that defines a function count_alpha_digits() that accepts a string and calculates the number of alphabets and digits in it. It should return these values as a dictionary.

def count_alpha_digits(string):
    alpha = 0
    digits = 0
    for char in string:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            digits += 1
    return {'alpha': alpha, 'digits': digits}

string = "Hello World! 123"
result = count_alpha_digits(string)
print(result)
