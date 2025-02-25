a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
if a>b and a>c:
    print(a," is greater")
    if b>c:
        print(c , " is smaller")
    else:
        print(a," is smaller")
elif b>a and b>c:
    print(b , " is greater")
    if a>c:
        print(c , " is smaller")
    else:
        print(a," is smaller")
elif c>a and c>b:
    print(c," is greater")
    if a>b:
        print(b," is smaller")
    else:
        print(a,(" is smaller"))
else:
    print("Invalid entry")