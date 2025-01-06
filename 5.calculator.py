

operator = input("Enter operator (+, -, *, /): ")
if operator not in ["+", "-", "*", "/"]:
    print("Invalid operator.")
    exit()
  
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
else:
    print(f"{num1} / {num2} = {num1 / num2}")
    