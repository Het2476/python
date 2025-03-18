# A palindrome is a word or phrase that reads the same in both directions. Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not. Ignore spaces and case mismatch while checking for palindrome.

def ispalindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


string = "Hello There"
print(ispalindrome(string))
