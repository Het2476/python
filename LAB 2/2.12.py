import math

def circle(x, y, r, a, b):
    distance = math.sqrt(math.pow(a - x, 2) + math.pow(b - y, 2))
    if distance < r:
        return "Inside the circle"
    elif distance == r:
        return "On the circle"
    else:
        return "Outside the circle"
x = int(input("Enter the x-coordinate of the center of the circle: "))
y = int(input("Enter the y-coordinate of the center of the circle: "))
r = int(input("Enter the radius of the circle: "))
a = int(input("Enter the x-coordinate of the point: "))
b = int(input("Enter the y-coordinate of the point: "))
result = circle(x, y, r, a, b)
print(result) 