def peri(l,b):
    p = 2*(l+b)
    area = l*b
    if p > area:
        print("perimeter is greater than area")
    else:        
        print("area is greater than perimeter")
l = int(input("Enter the length "))
b = int(input("Enter the breadth "))
peri(l,b)