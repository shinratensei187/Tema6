from termcolor import colored

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError(colored("Division by zero is not allowed.", "red"))
    return a / b

if __name__ == "__main__":
    print(f"Addition result: {add(4, 2)}")
    print(f"Subtraction result: {subtract(4, 2)}")
    print(f"Multiplication result: {multiply(4, 2)}")
    print(f"Division result: {divide(4, 2)}")
