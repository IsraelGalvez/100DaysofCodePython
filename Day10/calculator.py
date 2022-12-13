# Calculator
from art import logo
#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)
        
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    answer = operation[operation_symbol](num1, num2)
    def new_operation():
        next_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        return next_operation

    should_continue = new_operation()
    while(should_continue == "y"):
        num1 = answer
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the second number?: "))
        answer = operation[operation_symbol](num1, num2)
        should_continue = new_operation()

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if should_continue == "n":
            calculator()

calculator()