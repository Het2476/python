def lc(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def uc(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def tc(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
s = input("Enter a string: ")
print(lc(s))  
print(uc(s))  
print(tc(s))    