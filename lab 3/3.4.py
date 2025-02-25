def remove(str1, remove):
    return str1.replace(remove, '')


str1 = input("Enter a string: ")
remove = input("Enter a string to remove: ")
final = remove(str1, remove)
print(final)