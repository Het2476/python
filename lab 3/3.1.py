def vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
str = input("Enter a string: ")
cnt = vowels(str)
print(f"The number of vowels in the string is: {cnt}")