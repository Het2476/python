# Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

def frequency(string):
    words = string.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items())

string = "Quick brown fox jumps over the lazy dog"
print(frequency(string))
