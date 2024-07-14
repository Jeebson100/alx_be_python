# File: temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    temperature = float(input("Enter the temperature: "))
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
