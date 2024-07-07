# File: multiplication_table.py

def main():
    # Prompting user for input
    number = int(input("Enter a number to see its multiplication table: "))

    # Generating and printing the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
