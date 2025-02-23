num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

operations = ["+", "-", "*", "/"]  # List of valid operators

match op:
    case "+":  
        print("Result:", num1 + num2)
    case "-":  
        print("Result:", num1 - num2)
    case "*":  
        print("Result:", num1 * num2)
    case "/":  
        print("Result:", "Error: Division by zero!" if num2 == 0 else num1 / num2)
    case _:  
         print("Invalid operator!")
