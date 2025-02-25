a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if a>b:
    print(a," is greater")
    print(b," is smaller")
elif b>a:
    print(b," is greater")
    print(a," is smaller")
else:
    print("Both are equal")