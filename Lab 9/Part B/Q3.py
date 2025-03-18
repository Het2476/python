# A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.

def count_vowels(string):
    if string == '':
        return 0
    if string[0].lower() in 'aeiou':
        return 1 + count_vowels(string[1:])
    return count_vowels(string[1:])

string = input("Enter a string: ")
print(count_vowels(string))
