# Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether a given string is pangram or not, through a user-defined function ispangram(). Test the function with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite opal jewels”. Hint: use set() to convert the string into a set of characters present in the string and use <= to check whether alphaset is a subset of the given string

def ispangram(string):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(string.lower())


string = "The quick brown fox jumps over the lazy dog"
print(ispangram(string))
