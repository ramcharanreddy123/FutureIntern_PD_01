def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    else:
        print("Invalid choice")

calculator()