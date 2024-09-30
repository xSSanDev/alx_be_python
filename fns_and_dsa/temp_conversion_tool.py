FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        temp = int(input("Enter the temperature to convert: "))
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if temp_type not in ["C", "F"]:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        if temp_type == "C":
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        if temp_type == "F":
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")

    except ValueError as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    main()
