# Write a recursive function to obtain length of a given string.

def length(string):
    if string == '':
        return 0
    return 1 + length(string[1:])


string = input("Enter a string: ")
print(length(string))
