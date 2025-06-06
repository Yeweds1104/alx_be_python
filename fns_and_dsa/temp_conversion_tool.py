FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

try:
    temp = float(input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temp_unit.lower() == "c":
        new_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {new_temp}°F")
    elif temp_unit.lower() == "f":
        new_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {new_temp}°C")
    else:
        print("Invalid temperature unit. Please enter 'C' or 'F'.")
    
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    
