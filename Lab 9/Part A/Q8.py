# Write a program that defines a function convert() that receives a string containing a sequence of whitespace separated words and returns a string after removing all duplicate words and sorting them alphanumerically. Hint: use set(), list () , sorted(), join().

def convert(string):
    return ' '.join(sorted(set(string.split())))


string = "Quick brown fox jumps over the lazy dog"
print(convert(string))
