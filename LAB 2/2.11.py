def slope(x1, y1, x2, y2, x3, y3):
    s1 = (y2-y1)/(x2-x1)
    s2 = (y3-y2)/(x3-x2)
    s3 = (y3-y1)/(x3-x1)
    if s1 == s2 and s2 == s3:
        return True
    else:
        return False

x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
x3, y3 = int(input("Enter x3: ")), int(input("Enter y3: "))

if slope(x1, y1, x2, y2, x3, y3):
    print("The points are collinear.")
else:
    print("The points are not collinear.")