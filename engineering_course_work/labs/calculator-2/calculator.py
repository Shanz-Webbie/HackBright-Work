"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


# create dictionary to asbstract different equations
operations_dict ={"+":add,
                  "-":subtract,
                  "*":multiply,
                  "/":divide,
                  "square":square,
                  "cube":cube,
                  "pow":power,
                  "mod":mod
                  }

def compute_equation(operator, num1, num2=None):
    if operator in operations_dict:
        # if a second number is not provided run the operation with one argument
        if num2 is None:
            return operations_dict[operator](num1)
        else:
            return operations_dict[operator](num1, num2)
    # if an operator and num(s) are not provided - print an error message
    else:
        raise ValueError("Invalid operator. Please try again.")


while True:
    # ask for user to type in a math operation
    user_input = input("What math operation would you like to perform? Input operator followed by numbers.")
    # extract the input numbers that are separated with a space
    user_equation = user_input.split(' ')
    # assign the math operator to be the first item input
    operator = user_equation[0]
    # stop the loop if user inputs q or quit
    if user_input.lower() == "q" or user_input.lower() == "quit":
        print("Goodbye!")
        break
        
    elif len(user_equation) >= 2:
        try:
            num1 = float(user_equation[1])
            if len(user_equation) == 3:
                num2 = float(user_equation[-1])
                result = compute_equation(operator, num1, num2)
            else:
                result = compute_equation(operator, num1)
            print(result)            
        except ValueError:
            print("There was an error with your input.")
        except ZeroDivisionError:
            ("You can't divide by zero.")
    else:
        print("Invalid input format. Please input operator followed by two numbers.")