def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose an operation: +, -, *, /")
    
    op = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation selected.")
        return
    
    print(f"Result: {result}")

calculator()