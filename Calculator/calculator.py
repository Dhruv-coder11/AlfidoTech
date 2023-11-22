class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"


def main():
    # Create an instance of the Calculator class
    calculator = Calculator()

    while True:
        # Take user input for operation choice
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1, 2, 3, 4, 5): ")

        # Exit the loop if the user chooses to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Take user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation using the Calculator object
        if choice == '1':
            result = calculator.add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = calculator.divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid input. Please enter a valid choice.")

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()

