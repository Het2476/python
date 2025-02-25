def check(x,y,z):
    if x+y+z == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

x = int(input("Enter the first angle "))
y = int(input("Enter the second angle "))
z = int(input("Enter the third angle "))
check(x,y,z)
