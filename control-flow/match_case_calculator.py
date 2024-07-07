# File: match_case_calculator.py

def main():
    # Prompting user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Performing the calculation using match case
    match operation:
        case '+':
            result = num1 + num2
            operation_str = "addition"
        case '-':
            result = num1 - num2
            operation_str = "subtraction"
        case '*':
            result = num1 * num2
            operation_str = "multiplication"
        case '/':
            if num2 != 0:
                result = num1 / num2
                operation_str = "division"
            else:
                print("Error: Division by zero is not allowed.")
                return
        case _:
            print(f"Error: '{operation}' is not a valid operation.")
            return

    # Output the result
    print(f"The result of {operation_str} of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
