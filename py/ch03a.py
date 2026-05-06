#Simple Calculator

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation."
print(f"The result is: {result}")

