from day8_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

options = {"+": add,
           "-": subtract,
           "*": multiply,
           "/": divide}

def calculator(num1, op, num2):
    """Takes two values and carries out mathmatical equation
    based on selected operator"""
    for i in options:
        if i == op:
            function = options[i]
            result = function(num1, num2)
    return f"The answer to {num1} {op} {num2} is {result}"

print(logo)
go = 'yes'
while go == 'yes':
    number1 = float(input("Input a number :"))
    for key in options:
        print(key)
    operator = str(input("Choose an operator :"))
    number2 = float(input("Input another number :"))

    answer = calculator(number1, operator, number2)
    print(answer)
    go = input("Do you want to go again? yes or no:")

print("goodbye!")
