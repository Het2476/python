a=int(input("Enter the 1st num"))
b=int(input("Enter the 2nd num"))
c=int(input("Enter the 3rd num"))
def largest ():
    if a>b and a>c:
        if b<c:
            print(a, "is the largest")
            print(b, "is the smallest")
    elif b>a and b>c:
        if c<a:
             print(b, "is the largest")
             print(c, "is the smallest")
    elif c>a and c>b:
        if a<b:
            print(c, "is the largest")
            print(a, "is the smallest")
    else:
        print("all r equal")
largest()
