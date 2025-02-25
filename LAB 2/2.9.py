def abso(num):
    if num < 0:
        return -num
    else:
        return num
num = int(input("Enter a number: "))
print("The absolute value of", num, "is", abso(num))