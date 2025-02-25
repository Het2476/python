def check(str1, str2):
    if str1 in str2:
        return True
    elif str2 in str1:
        return True
    else:
        return False


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(check(string1, string2))  

