#CODE 1: Write a program that receives an integer an input. If a string is entered instead of an integer, then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied

def get_integer_input():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Example usage
if __name__ == "__main__":
    integer_value = get_integer_input()
    print(f"You entered the integer: {integer_value}")
