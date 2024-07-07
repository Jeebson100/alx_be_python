# File: pattern_drawing.py

def main():
    # Prompting user for input
    size = int(input("Enter the size of the pattern: "))

    # Drawing the pattern
    row = 1
    while row <= size:
        # Print '*' for each column in the current row
        for col in range(size):
            print("*", end="")
        # Move to the next line after printing all columns in the current row
        print()
        row += 1

if __name__ == "__main__":
    main()
