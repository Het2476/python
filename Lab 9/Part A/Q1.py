# Write a Program that defines a function count_lower_upper() that accepts a string and calculates the number of lowercase and uppercase characters in the string. The function should return a dictionary with two keys: 'upper' and 'lower' and their corresponding values. The function should ignore any characters that are not alphabets. It should return these values as a dictionary. Call this function for some sample string

def count_lower_upper(string):
    lower = 0
    upper = 0
    for char in string:
        if char.isalpha():
            if char.islower():
                lower += 1
            else:
                upper += 1
    return {'upper': upper, 'lower': lower}

string = "Hello World! 123"
result = count_lower_upper(string)
print(result)
