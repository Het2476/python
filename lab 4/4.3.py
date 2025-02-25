def count(str1):
    alphabets = 0
    digits = 0

    for char in str1:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1

    return alphabets, digits

str1 = input("Enter a string: ")
alphabets, digits = count(str1)
print(f"Alphabets: {alphabets}, Digits: {digits}")