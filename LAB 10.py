#CODE 1: Write a program to create a csv file that we can directly open in MS-Excel

import csv

with open("Q1.csv", "wb") as f:
    f.write(b"Name,Age,City\n")
    f.write(b"Alice,30,New York\n")
    f.write(b"Bob,25,Los Angeles\n")
with open("Q1.csv", "rb") as f:
    for line in f:
        print(line.decode().strip())


#CODE 2: Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.

import csv

with open("Q2.csv", "r") as f:
    reader = csv.DictReader(f)
    
    data = []
    for row in reader:
        
        row['CPII'] = int(row['CPII'])
        row['MathsII'] = int(row['MathsII'])
        row['Chemistry'] = int(row['Chemistry'])
        row['total'] = row['CPII'] + row['MathsII'] + row['Chemistry']
        data.append(row)
    
    for record in data:
        print(record)



#CODE 3: Accept contact details from the user and create a vcard that we can directly store in our mobile.

import csv

with open("Q3.vcf", "w") as f:
    
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    
   
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    
    
    f.write(f"N:{name}\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    
   
    f.write("END:VCARD\n")


#CODE 4: Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory

import os

current_path = os.getcwd()
subdirectory = os.path.join(current_path, 'Q4')
if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)
    print(f"Directory {subdirectory} created.")
else:
    print(f"Directory {subdirectory} already exists.")

source_file = os.path.join(current_path, 'Q3', 'Q3.py')
destination_file = os.path.join(subdirectory, 'Q3.py')
if os.path.exists(source_file):
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"File copied from {source_file} to {destination_file}.")
else:
    print(f"Source file {source_file} does not exist.")


#CODE 5: Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.

with open("Q5.txt", "r") as source_file:
    content = source_file.read()
    upper_content = content.upper()
    with open("Q5_copy.txt", "w") as destination_file:
        destination_file.write(upper_content)
    print("File copied and converted to uppercase.")


#CODE 6: Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.


with open("Q6_file1.txt", "r") as file1, open("Q6_file2.txt", "r") as file2, open("Q6_merged.txt", "w") as merged_file:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        if i < len(lines1):
            merged_file.write(lines1[i])
        if i < len(lines2):
            merged_file.write(lines2[i])

print("Files merged successfully into Q6_merged.txt.")


#CODE 7: If an Employee object contains following details:empcode, empname, Date of Joining, Salary.Write a program to serialize and deserialize this data.

import pickle


class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.date_of_joining}, Salary: {self.salary}"


def serialize_employee(employee, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)


def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        employee = pickle.load(file)
    return employee


emp1 = Employee("E001", "Joe Mama", "2023-01-01", 50000)
serialize_employee(emp1, "employee.dat")

deserialized_emp = deserialize_employee("employee.dat")
print(deserialized_emp)


#CODE 8: Given a text file, write a program to create another text file deleting the words "a", "the", "an" and replacing each one of them with a blank space.

with open("Q8.txt", "r") as file:
    content = file.read()

print("Original Content:")
print(content)

words_to_replace = ["a", "the", "an"]

for word in words_to_replace:
    content = content.replace(word, " ")

print("\nModified Content:")
print(content)

with open("Q8_modified.txt", "w") as file:
    file.write(content)

print("\nModified content written to Q8_modified.txt")

with open("Q8_modified.txt", "r") as file:
    modified_content = file.read()

print("\nModified Content Read from Q8_modified.txt:")
print(modified_content)
