#CODE 1: Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition, subtraction, multiplication and division.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                             (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i" if self.imaginary >= 0 else f"{self.real} - {-self.imaginary}i"


c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
print("Complex Number 1:", c1)
print("Complex Number 2:", c2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)


#CODE 2: Write a program that implements a Matrix class and performs addition, multiplication and transpose operations on 3x3 matrices.
class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        return Matrix([[self.elements[i][j] + other.elements[i][j] for j in range(3)] for i in range(3)])

    def __mul__(self, other):
        return Matrix([[sum(self.elements[i][k] * other.elements[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def transpose(self):
        return Matrix([[self.elements[j][i] for j in range(3)] for i in range(3)])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.elements])


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Addition of Matrix 1 and Matrix 2:")
print(matrix1 + matrix2)
print("Multiplication of Matrix 1 and Matrix 2:")
print(matrix1 * matrix2)
print("Transpose of Matrix 1:")
print(matrix1.transpose())
print("Transpose of Matrix 2:")
print(matrix2.transpose())


#CODE 3: Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid

class Solid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self):
        return self.length * self.width * self.height


solid = Solid(2, 3, 4)
print("Surface Area:", solid.surface_area())
print("Volume:", solid.volume())



#CODE 4: Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape

class Shape:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == "circle":
            radius = self.dimensions[0]
            return 3.14 * radius ** 2
        elif self.shape_type == "rectangle":
            length, width = self.dimensions
            return length * width
        elif self.shape_type == "square":
            side = self.dimensions[0]
            return side ** 2
        else:
            raise ValueError("Unknown shape type")

    def perimeter(self):
        if self.shape_type == "circle":
            radius = self.dimensions[0]
            return 2 * 3.14 * radius
        elif self.shape_type == "rectangle":
            length, width = self.dimensions
            return 2 * (length + width)
        elif self.shape_type == "square":
            side = self.dimensions[0]
            return 4 * side
        else:
            raise ValueError("Unknown shape type")


# Example usage
shape1 = Shape("circle", 5)
shape2 = Shape("rectangle", 4, 6)
shape3 = Shape("square", 3)
print(f"Circle Area: {shape1.area()}, Perimeter: {shape1.perimeter()}")
print(f"Rectangle Area: {shape2.area()}, Perimeter: {shape2.perimeter()}")
print(f"Square Area: {shape3.area()}, Perimeter: {shape3.perimeter()}")



#CODE 5: Write a program that creates and uses a Time class to perform various time arithmetic operations.
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def subtract(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) - \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        if total_seconds < 0:
            total_seconds += 24 * 3600
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def multiply(self, factor):
        total_seconds = (self.hours * 3600 + self.minutes *
                         60 + self.seconds) * factor
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def divide(self, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        total_seconds = (self.hours * 3600 + self.minutes *
                         60 + self.seconds) // divisor
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


# Example usage
time1 = Time(2, 30, 45)
time2 = Time(1, 15, 20)
print("Time 1:", time1)
print("Time 2:", time2)
print("Addition:", time1.add(time2))
print("Subtraction:", time1.subtract(time2))
print("Multiplication by 2:", time1.multiply(2))
print("Division by 2:", time1.divide(2))
print("Time 1 in seconds:", time1.to_seconds())
print("Time 2 in seconds:", time2.to_seconds())


#CODE 6: Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.day == other.day and
                self.month == other.month and
                self.year == other.year)

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"


# Example usage
date1 = Date(15, 8, 2023)
date2 = Date(15, 8, 2023)
date3 = Date(16, 8, 2023)

print("Date 1:", date1)
print("Date 2:", date2)
print("Date 3:", date3)
print("Date 1 == Date 2:", date1 == date2)  
print("Date 1 == Date 3:", date1 == date3)  


#CODE 7: Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)

class Weather:

    def __init__(self, temperature, humidity, wind_speed):
        self.weather_parameters = {
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
        }

    def __contains__(self, item):
        return item in self.weather_parameters.values()

    def __str__(self):
        return f"Weather Parameters: {self.weather_parameters}"


# Example usage
weather = Weather(temperature=30, humidity=70, wind_speed=15)
print(weather)
print("Is 30 in weather parameters?", 30 in weather)  
print("Is 25 in weather parameters?", 25 in weather) 

#CODE 8:Implement a String class containing the following functions:a. Overloaded += operator function to perform string concatenationb. Method toLower() to convert upper case letters to lower case.c. Method toUpper() to convert lower case letters to upper case.



class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        else:
            self.value += str(other)
        return self

    def toLower(self):
        self.value = self.value.lower()
        return self

    def toUpper(self):
        self.value = self.value.upper()
        return self


# Example usage
if __name__ == "__main__":
    str1 = String("Hello")
    str2 = String(" World")
    str1 += str2
    print(str1.value)  

    str1.toLower()
    print(str1.value)  

    str1.toUpper()
    print(str1.value) 
    str1 += "!"
    print(str1.value) 
    str1 += 123
    print(str1.value)  
    str1 += str2
    print(str1.value)  
