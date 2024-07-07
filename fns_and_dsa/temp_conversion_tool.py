# File: temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        
        scale = input("Enter the scale of the temperature (C for Celsius, F for Fahrenheit): ").strip().upper()

        if scale == 'F':
            celsius_temp = convert_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is {celsius_temp:.2f} Celsius.")
        elif scale == 'C':
            fahrenheit_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is {fahrenheit_temp:.2f} Fahrenheit.")
        else:
            print("Invalid scale. Please enter 'C' or 'F'.")

        choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting temperature conversion tool. Goodbye!")
            break

if __name__ == "__main__":
    main()
