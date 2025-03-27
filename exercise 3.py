def main():
    while True:
        print("Welcome to the Simple Calculator!")
        print("Please choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Simulating a do...while loop
        choice = 0
        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if 1 <= choice <= 5:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break

        # Nested while loop for performing the selected operation
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    result = num1 + num2
                    print(f"The result of {num1} + {num2} is {result}.")
                elif choice == 2:
                    result = num1 - num2
                    print(f"The result of {num1} - {num2} is {result}.")
                elif choice == 3:
                    result = num1 * num2
                    print(f"The result of {num1} * {num2} is {result}.")
                elif choice == 4:
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        print(f"The result of {num1} / {num2} is {result}.")
                
                # Break the nested loop after performing the operation
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()