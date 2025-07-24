# Calculator

import art
import math
import sys

def add(n1 ,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def root(n1, n2):
    return n1 ** (1/n2)

def log(n1, n2):
    return math.log(n1, n2)

def trignometry(n1, n2):
    trig_variable = True
    while trig_variable:
        if n2 == 0:
            return math.sin(n1)
        elif n2 == 1:
            return math.cos(n1)
        elif n2 == 2:
            return math.tan(n1)
        elif n2 == 3:
            return math.sinh(n1)
        elif n2 == 4:
            return math.cosh(n1)
        elif n2 == 5:
            return math.tanh(n1)
        else:
            print("Choose correct option.")

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "|": root,
    "log": log,
    "trig": trignometry
}

operations_choice = {
    "+": "Enter number to add:",
    "-": "Enter number to subtract:",
    "*": "Enter number to multiply:",
    "/": "Enter number to divide:",
    "^": "Enter power to raise:",
    "|": "Enter 'n' for nth root:",
    "log": "Enter base:",
    "trig": "Choose any one:"
}

trig_choice = {
    "Sin": 0,
    "Cos": 1,
    "Tan": 2,
    "Sinh": 3,
    "Cosh": 4,
    "Tanh": 5
}

def calculations():
    print(art.logo)
    result = 0
    calc_over = True
    while calc_over:
        if result != 0:
            a = result
        else:
            a = float(input("Enter number (Angle Degree if trignometry):"))

        print("Choose an operation: ")
        for symbol in operations_dict:
            if symbol == list(operations_dict)[-1]:
                print(symbol)
            else:
                print(symbol, end=", ")

        op_correction = True
        while op_correction:
            op = input()
            if op not in operations_dict:
                print("Choose a correct operation:")
            else:
                op_correction= False

        print(operations_choice[op])
        if op == "trig":
            a_format = input("Deg for Degree and Rad for Radian: ").lower()
            if a_format == "deg":
                a = math.radians(a)
            else:
                pass
            for key in trig_choice:
                print(f"{key}: {trig_choice[key]}")

        b = float(input())
        result = operations_dict[op](a, b)
        print(f"{result:.3f}")

        choice_correction = True
        while choice_correction:
            choice = input("""Enter 'y' to continue with result, 'n' for new calculation, or 'exit' to close: """).lower()
            if choice == "y":
                choice_correction = False
                pass
            elif choice == "n":
                choice_correction = False
                result = 0
                calc_over = False
                print("\n" * 20)
                calculations()
            elif choice == "exit":
                sys.exit()
            else:
                print("Kindly choose the correct option.")

calculations()

#----------------------------------------- art.py -----------------------------------------#
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|  
"""

