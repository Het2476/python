#CODE 1: Write a program to create three dictionaries and concatenate them to create fourth dictionary.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
dict4 = {**dict1, **dict2, **dict3}
print(dict4)

#CODE 2: Write a program to check whether a dictionary is empty or not.

dict1 = {'key1': 'value1', 'key2': 'value2'}
if not dict1:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")


#CODE 3: Create a dictionary in python with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.

dict1 = {
    'dept1': {'roll_no': 101, 'salary': 50000},
    'dept2': {'roll_no': 102, 'salary': 60000},
    'dept3': {'roll_no': 103, 'salary': 55000},
}


def find_min_max_salary(dept_dict):
    min_salary = float('inf')
    max_salary = float('-inf')
    for dept, info in dept_dict.items():
        salary = info['salary']
        if salary < min_salary:
            min_salary = salary
        if salary > max_salary:
            max_salary = salary
    return min_salary, max_salary


min_salary, max_salary = find_min_max_salary(dict1)
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")


#CODE 4: Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.

def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    frequency_dict = char_frequency(input_string)
    print("Character frequency:", frequency_dict)


#CODE 5: Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

grocery_prices = {
    'apple': 2.5,
    'banana': 1.0,
    'orange': 1.5,
    'milk': 3.0,
    'bread': 2.0
}
grocery_quantities = {
    'apple': 3,
    'banana': 5,
    'orange': 2,
    'milk': 1,
    'bread': 4
}


def calculate_total_bill(prices, quantities):
    total_bill = 0
    for item, price in prices.items():
        if item in quantities:
            total_bill += price * quantities[item]
    return total_bill


total_bill = calculate_total_bill(grocery_prices, grocery_quantities)
print(f"Total bill: ${total_bill:.2f}")  
