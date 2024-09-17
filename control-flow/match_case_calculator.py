num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
if operation == "+":
    result = num1 + num2
    print(f"The result is {result}.")
elif operation == "-":
    result = num1 - num2
    print(f"The result is {result}.")
elif operation == "*":
    result = num1 * num2
    print(f"The result is {result}.")
elif operation == "/" and num2 != 0:
    result = num1 / num2
    print(f"The result is {result}.")
elif operation == "/" and num2 == 0:
    print("Cannot divide by zero.")
