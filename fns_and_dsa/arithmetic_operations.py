def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."

# Ensure the module can be imported without executing code
if __name__ == "__main__":
    # Example usage (this section won't run when imported)
    print(perform_operation(4, 2, 'add'))        # Output: 6
    print(perform_operation(4, 2, 'subtract'))   # Output: 2
    print(perform_operation(4, 2, 'multiply'))   # Output: 8
    print(perform_operation(4, 2, 'divide'))     # Output: 2.0
    print(perform_operation(4, 0, 'divide'))     # Output: Error: Division by zero is not allowed.
    print(perform_operation(4, 2, 'modulus'))    # Output: Error: Invalid operation.